"""RSS Reader command line interface application."""

import logging
from rss_reader import RssReader, NoFeedsFound, EncodingException, NonXmlTypeException

from .ArgsParser import ArgsParser

from .writter.DefaultWritter import DefaultWritter
from .writter.FileWritter import FileWritter

from .formatter.Format import Format
from .formatter.get_formatter import get_formatter


def main():
    params = ArgsParser().parse_args()

    logging.basicConfig(level=params.log_level)

    rss_reader = RssReader()
    formatter = get_formatter(Format.JSON) if params.json else get_formatter()
    writter = DefaultWritter()

    logging.info(f"reading RSS feed from {params.source}")
    try:
        feed_entries = rss_reader.read(params)
    except NoFeedsFound:
        print("No feeds found")
        return
    except EncodingException:
        print("Error while reading feed. Encoding issue")
        return
    except NonXmlTypeException:
        print("The feed has wrong format. XML format is expected")
        return
    except Exception:
        print("Unable to read feed due to unknown exception")
        return

    logging.info("formatting feed entries")
    output = formatter.format(feed_entries)

    writter.write(output)

    if params.output_file:
        logging.info(f"writting feed to the file: {params.output_file}")
        file_writter = FileWritter(params.output_file)
        formatter = get_formatter(params.output_file_format)

        file_content = formatter.format(feed_entries)

        try:
            file_writter.write(file_content)
        except Exception:
            print("Error while writting to the file")


if __name__ == "__main__":
    main()
