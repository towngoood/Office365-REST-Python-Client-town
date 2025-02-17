from generator import load_settings
from generator.builders.type_builder import TypeBuilder
from office365.runtime.odata.v3.metadata_reader import ODataV3Reader
from office365.runtime.odata.v4.metadata_reader import ODataV4Reader
import logging

def generate_files(model, options):
    """
    Generate files based on the OData model and configuration settings.
    
    :param model: OData model object
    :type model: office365.runtime.odata.model.ODataModel
    :param options: Configuration settings
    :type options: ConfigParser
    """
    for name in model.types:
        type_schema = model.types[name]
        builder = TypeBuilder(type_schema, options)
        builder.build()
        if builder.status == "created":
            builder.save()
            logging.info(f"File for type '{name}' created and saved.")
        else:
            logging.warning(f"File for type '{name}' could not be created, status: {builder.status}")

def generate_sharepoint_model(settings):
    """
    Generate SharePoint model based on OData metadata.
    
    :param settings: Configuration settings
    :type settings: ConfigParser
    """
    try:
        reader = ODataV3Reader(settings.get("sharepoint", "metadataPath"))
        reader.format_file()
        model = reader.generate_model()
        generate_files(model, settings)
    except Exception as e:
        logging.error(f"Error generating SharePoint model: {e}")

def generate_graph_model(settings):
    """
    Generate Microsoft Graph model based on OData metadata.
    
    :param settings: Configuration settings
    :type settings: ConfigParser
    """
    try:
        reader = ODataV4Reader(settings.get("microsoftgraph", "metadataPath"))
        model = reader.generate_model()
        generate_files(model, settings)
    except Exception as e:
        logging.error(f"Error generating Microsoft Graph model: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    generator_settings = load_settings()
    
    # Choose which model to generate: SharePoint or Microsoft Graph
    try:
        model_choice = generator_settings.get("settings", "modelChoice").lower()
        if model_choice == "sharepoint":
            generate_sharepoint_model(generator_settings)
        elif model_choice == "microsoftgraph":
            generate_graph_model(generator_settings)
        else:
            logging.error("Invalid model choice in settings. Please specify either 'sharepoint' or 'microsoftgraph'.")
    except Exception as e:
        logging.error(f"Error loading settings or deciding model choice: {e}")

if __name__ == "__main__":
    main()
