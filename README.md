# Multiuse-Spider
A scraping algorithm that extracts all tags from a website and organizes the tags and their attributes in a dictionary. The implementation is written in python, long, repetitive, inefficient and could be done better but it does the job quite well in a short amount of time and works with any website it can get through to. Enjoy :)

Object is instantiated with any url passed to it e.g. spider = Spider("https://google.com"), using the method scrape will scrape
the site and store the data in attribute parse_dict
parse_dict is structured in form 
{
  <tag>: [
            {
              <attribs>: <values>
             }
         ]
}
Method sort_structure takes input data which is any list of attributes stored in a tag stored in parse_dict. Example call sort_structure(self.parse_dict['a'])
		with self.parse_dict['a'] being list of attributes found in every a tag; i.e. {'a': 
													[
														{'class': ['svg', 'btn'], 'href': '/modal', 'text': 'Text inside tag'},
														{'class': ['btn'], 'href': '#', 'text: ''}
													]
		alpha returns data in form{
						<tag>: {
								<index-letter>: {
											<attrib-name>: [
														<value>
													]
										}
							}
					}
		with index-letter being the first letter of attributes it encounters, attrib-name being the name of attributes with index-letter as their first letter and value being a sorted list of all values found of said attribute
		eg output using example input above: {
							'a': {
								'c': {
									'class': '['btn', 'svg']
									},
								'h': {
									'href': ['#', '/modal']
									},
								't': {
									'text': ['Text inside tag', '']
									}
								}
							}
