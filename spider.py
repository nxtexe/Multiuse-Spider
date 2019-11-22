from bs4 import BeautifulSoup
import requests


class Spider():
	def __init__(self, url):
		self.url = url
		self.headers={
								'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
								'Accept-Encoding': 'gzip, deflate, br',
								'Accept-Language': 'en-US,en;q=0.9',
								'Cache-Control': 'max-age=0',
								'Connection': 'keep-alive',
								'Cookie': 'PHPSESSID=qbseddpciibh2tnmtca7a4ji50; _ga=GA1.2.267392348.1573700540; _gid=GA1.2.1833252340.1574293599',
								'Host': 'isbnsearch.org',
								'Referer': 'https://isbnsearch.org/isbn/0395874521',
								'Sec-Fetch-Mode': 'navigate',
								'Sec-Fetch-Site': 'none',
								'Sec-Fetch-User': '?1',
								'Upgrade-Insecure-Requests': '1',
								'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
		self.parse_dict = {}

	def scrape(self):
		request = requests.get(self.url, self.headers)
		self.parse(request.text)

	def parse(self, response):
		main_soup = BeautifulSoup(response, "html.parser")
		#extract a tags and their attributes
		a_selectors =  main_soup.find_all('a')
		if a_selectors != []:
			self.parse_dict['a'] = []
			for a in a_selectors:
				info_dict = {}
				info_dict = a.attrs
				info_dict['text'] = a.text.strip()
				self.parse_dict['a'].append(info_dict)
		#extract abbr tags and their attributes
		abbr_selectors = main_soup.find_all('abbr')
		if abbr_selectors != []:
			self.parse_dict['abbr'] = []
			for abbr in abbr_selectors:
				info_dict = {}
				info_dict = abbr.attrs
				info_dict['text'] = abbr.text.strip()
				self.parse_dict['abbr'].append(info_dict)
		#extract acronym tags and their attributes
		acronym_selectors = main_soup.find_all('acronym')
		if acronym_selectors != []:
			self.parse_dict['acronym'] = []
			for acronym in acronym_selectors:
				info_dict = {}
				info_dict = acronym.attrs
				info_dict['text'] = acronym.text.strip()
				self.parse_dict['acronym'].append(info_dict)
		#extract address tags and their attributes
		address_selectors = main_soup.find_all('address')
		if address_selectors != []:
			self.parse_dict['address'] = []
			for address in address_selectors:
				info_dict = {}
				info_dict = address.attrs
				info_dict['text'] = address.text.strip()
				self.parse_dict['address'].append(info_dict)
		#extract applet tags and their attributes
		applet_selectors = main_soup.find_all('applet')
		if applet_selectors != []:
			self.parse_dict['applet'] = []
			for applet in applet_selectors:
				info_dict = {}
				info_dict = applet.attrs
				info_dict['text'] = applet.text.strip()
				self.parse_dict['applet'].append(info_dict)
		#extract area tags and their attributes
		area_selectors = main_soup.find_all('area')
		if area_selectors != []:
			self.parse_dict['area'] = []
			for area in area_selectors:
				info_dict = {}
				info_dict = area.attrs
				info_dict['text'] = area.text.strip()
				self.parse_dict['area'].append(info_dict)
		#extract article tags and their attributes
		article_selectors = main_soup.find_all('article')
		if article_selectors != []:
			self.parse_dict['article'] = []
			for article in article_selectors:
				info_dict = {}
				info_dict = article.attrs
				info_dict['text'] = article.text.strip()
				self.parse_dict['article'].append(info_dict)
		#extract aside tags and their attributes
		aside_selectors = main_soup.find_all('aside')
		if aside_selectors != []:
			self.parse_dict['aside'] = []
			for aside in aside_selectors:
				info_dict = {}
				info_dict = aside.attrs
				info_dict['text'] = aside.text.strip()
				self.parse_dict['aside'].append(info_dict)
		#extract audio tags and their attributes
		audio_selectors = main_soup.find_all('audio')
		if audio_selectors != []:
			self.parse_dict['audio'] = []
			for audio in audio_selectors:
				info_dict = {}
				info_dict = audio.attrs
				info_dict['text'] = audio.text.strip()
				self.parse_dict['audio'].append(info_dict)
		#extract b tags and their attributes
		b_selectors = main_soup.find_all('b')
		if b_selectors != []:
			self.parse_dict['b'] = []
			for b in b_selectors:
				info_dict = {}
				info_dict = b.attrs
				info_dict['text'] = b.text.strip()
				self.parse_dict['b'].append(info_dict)
		#extract base tags and their attributes
		base_selectors = main_soup.find_all('base')
		if base_selectors != []:
			self.parse_dict['base'] = []
			for base in base_selectors:
				info_dict = {}
				info_dict = base.attrs
				info_dict['text'] = base.text.strip()
				self.parse_dict['base'].append(info_dict)
		#extract basefont tags and their attributes
		basefont_selectors = main_soup.find_all('basefont')
		if basefont_selectors != []:
			self.parse_dict['basefont'] = []
			for basefont in basefont_selectors:
				info_dict = {}
				info_dict = basefont.attrs
				info_dict['text'] = basefont.text.strip()
				self.parse_dict['basefont'].append(info_dict)
		#extract bdi tags and their attributes
		bdi_selectors = main_soup.find_all('bdi')
		if bdi_selectors != []:
			self.parse_dict['bdi'] = []
			for bdi in bdi_selectors:
				info_dict = {}
				info_dict = bdi.attrs
				info_dict['text'] = bdi.text.strip()
				self.parse_dict['bdi'].append(info_dict)
		#extract bdo tags and their attributes
		bdo_selectors = main_soup.find_all('bdo')
		if bdo_selectors != []:
			self.parse_dict['bdo'] = []
			for bdo in bdo_selectors:
				info_dict = {}
				info_dict = bdo.attrs
				info_dict['text'] = bdo.text.strip()
				self.parse_dict['bdo'].append(info_dict)
		#extract big tags and their attributes
		big_selectors = main_soup.find_all('big')
		if big_selectors != []:
			self.parse_dict['big'] = []
			for big in big_selectors:
				info_dict = {}
				info_dict = big.attrs
				info_dict['text'] = big.text.strip()
				self.parse_dict['big'].append(info_dict)
		#extract blockquote tags and their attributes
		blockquote_selectors = main_soup.find_all('blockquote')
		if blockquote_selectors != []:
			self.parse_dict['blockquote'] = []
			for blockquote in blockquote_selectors:
				info_dict = {}
				info_dict = blockquote.attrs
				info_dict['text'] = blockquote.text.strip()
				self.parse_dict['blockquote'].append(info_dict)
		#extract br tags and their attributes
		br_selectors = main_soup.find_all('br')
		if br_selectors != []:
			self.parse_dict['br'] = []
			for br in br_selectors:
				info_dict = {}
				info_dict = br.attrs
				info_dict['text'] = br.text.strip()
				self.parse_dict['br'].append(info_dict)
		#extract button tags and their attributes
		button_selectors = main_soup.find_all('button')
		if button_selectors != []:
			self.parse_dict['button'] = []
			for button in button_selectors:
				info_dict = {}
				info_dict = button.attrs
				info_dict['text'] = button.text.strip()
				self.parse_dict['button'].append(info_dict)
		#extract canvas tags and their attributes
		canvas_selectors = main_soup.find_all('canvas')
		if canvas_selectors != []:
			self.parse_dict['canvas'] = []
			for canvas in canvas_selectors:
				info_dict = {}
				info_dict = canvas.attrs
				info_dict['text'] = canvas.text.strip()
				self.parse_dict['canvas'].append(info_dict)
		#extract caption tags and their attributes
		caption_selectors = main_soup.find_all('caption')
		if caption_selectors != []:
			self.parse_dict['caption'] = []
			for caption in caption_selectors:
				info_dict = {}
				info_dict = caption.attrs
				info_dict['text'] = caption.text.strip()
				self.parse_dict['caption'].append(info_dict)
		#extract center tags and their attributes
		center_selectors = main_soup.find_all('center')
		if center_selectors != []:
			self.parse_dict['center'] = []
			for center in center_selectors:
				info_dict = {}
				info_dict = center.attrs
				info_dict['text'] = center.text.strip()
				self.parse_dict['center'].append(info_dict)
		#extract cite tags and their attributes
		cite_selectors = main_soup.find_all('cite')
		if cite_selectors != []:
			self.parse_dict['cite'] = []
			for cite in cite_selectors:
				info_dict = {}
				info_dict = cite.attrs
				info_dict['text'] = cite.text.strip()
				self.parse_dict['cite'].append(info_dict)
		#extract code tags and their attributes
		code_selectors = main_soup.find_all('code')
		if code_selectors != []:
			self.parse_dict['code'] = []
			for code in code_selectors:
				info_dict = {}
				info_dict = code.attrs
				info_dict['text'] = code.text.strip()
				self.parse_dict['code'].append(info_dict)
		#extract col tags and their attributes
		col_selectors = main_soup.find_all('a')
		if col_selectors != []:
			self.parse_dict['col'] = []
			for col in col_selectors:
				info_dict = {}
				info_dict = col.attrs
				info_dict['text'] = col.text.strip()
				self.parse_dict['col'].append(info_dict)
		#extract colgroup tags and their attributes
		colgroup_selectors = main_soup.find_all('colgroup')
		if colgroup_selectors != []:
			self.parse_dict['colgroup'] = []
			for colgroup in colgroup_selectors:
				info_dict = {}
				info_dict = colgroup.attrs
				info_dict['text'] =colgroup.text.strip()
				self.parse_dict['colgroup'].append(info_dict)
		#extract data tags and their attributes
		data_selectors = main_soup.find_all('data')
		if data_selectors != []:
			self.parse_dict['data'] = []
			for data in data_selectors:
				info_dict = {}
				info_dict = data.attrs
				info_dict['text'] = data.text.strip()
				self.parse_dict['data'].append(info_dict)
		#extract datalist tags and their attributes
		datalist_selectors = main_soup.find_all('datalist')
		if datalist_selectors != []:
			self.parse_dict['datalist'] = []
			for datalist in datalist_selectors:
				info_dict = {}
				info_dict = datalist.attrs
				info_dict['text'] = datalist.text.strip()
				self.parse_dict['datalist'].append(info_dict)
		#extract dd tags and their attributes
		dd_selectors = main_soup.find_all('dd')
		if dd_selectors != []:
			self.parse_dict['dd'] = []
			for dd in dd_selectors:
				info_dict = {}
				info_dict = dd.attrs
				info_dict['text'] = dd.text.strip()
				self.parse_dict['dd'].append(info_dict)
		#extract del tags and their attributes
		del_selectors = main_soup.find_all('del')
		if del_selectors != []:
			self.parse_dict['del'] = []
			for del_ in del_selectors:
				info_dict = {}
				info_dict = del_.attrs
				info_dict['text'] = del_.text.strip()
				self.parse_dict['del'].append(info_dict)
		#extract details tags and their attributes
		details_selectors = main_soup.find_all('details')
		if details_selectors != []:
			self.parse_dict['details'] = []
			for details in details_selectors:
				info_dict = {}
				info_dict = details.attrs
				info_dict['text'] = details.text.strip()
				self.parse_dict['details'].append(info_dict)
		#extract dfn tags and their attributes
		dfn_selectors = main_soup.find_all('dfn')
		if dfn_selectors != []:
			self.parse_dict['dfn'] = []
			for dfn in dfn_selectors:
				info_dict = {}
				info_dict = dfn.attrs
				info_dict['text'] = dfn.text.strip()
				self.parse_dict['dfn'].append(info_dict)
		#extract dialog tags and their attributes
		dialog_selectors = main_soup.find_all('dialog')
		if dialog_selectors != []:
			self.parse_dict['dialog'] = []
			for dialog in dialog_selectors:
				info_dict = {}
				info_dict = dialog.attrs
				info_dict['text'] = dialog.text.strip()
				self.parse_dict['dialog'].append(info_dict)
		#extract dir tags and their attributes
		dir_selectors = main_soup.find_all('dir')
		if dir_selectors != []:
			self.parse_dict['dir'] = []
			for dir_ in dir_selectors:
				info_dict = {}
				info_dict = dir_.attrs
				info_dict['text'] = dir_.text.strip()
				self.parse_dict['dir'].append(info_dict)
		#extract div tags and their attributes
		div_selectors = main_soup.find_all('div')
		if div_selectors != []:
			self.parse_dict['div'] = []
			for div in div_selectors:
				info_dict = {}
				info_dict = div.attrs
				info_dict['text'] = div.text.strip()
				self.parse_dict['div'].append(info_dict)
		#extract dl tags and their attributes
		dl_selectors =main_soup.find_all('dl')
		if dl_selectors != []:
			self.parse_dict['dl'] = []
			for dl in dl_selectors:
				info_dict = {}
				info_dict = dl.attrs
				info_dict['text'] = dl.text.strip()
				self.parse_dict['dl'].append(info_dict)
		#extract dt tags and their attributes
		dt_selectors = main_soup.find_all('dt')
		if dt_selectors != []:
			self.parse_dict['dt'] = []
			for dt in dt_selectors:
				info_dict = {}
				info_dict = dt.attrs
				info_dict['text'] = dt.text.strip()
				self.parse_dict['dt'].append(info_dict)
		#extract em tags and their attributes
		em_selectors = main_soup.find_all('em')
		if em_selectors != []:
			self.parse_dict['em'] = []
			for em in em_selectors:
				info_dict = {}
				info_dict = em.attrs
				info_dict['text'] = em.text.strip()
				self.parse_dict['em'].append(info_dict)
		#extract embed tags and their attributes
		embed_selectors = main_soup.find_all('embed')
		if embed_selectors != []:
			self.parse_dict['embed'] = []
			for embed in embed_selectors:
				info_dict = {}
				info_dict = embed.attrs
				info_dict['text'] = embed.text.strip()
				self.parse_dict['embed'].append(info_dict)
		#extract fieldset tags and their attributes
		fieldset_selectors = main_soup.find_all('fieldset')
		if fieldset_selectors != []:
			self.parse_dict['fieldset'] = []
			for fieldset in fieldset_selectors:
				info_dict = {}
				info_dict = fieldset.attrs
				info_dict['text'] = fieldset.text.strip()
				self.parse_dict['fieldset'].append(info_dict)
		#extract figcaption tags and their attributes
		figcaption_selectors = main_soup.find_all('figcaption')
		if figcaption_selectors != []:
			self.parse_dict['figcaption'] = []
			for figcaption in figcaption_selectors:
				info_dict = {}
				info_dict = figcaption.attrs
				info_dict['text'] = figcaption.text.strip()
				self.parse_dict['figcaption'].append(info_dict)
		#extract figure tags and their attributes
		figure_selectors = main_soup.find_all('figure')
		if figure_selectors != []:
			self.parse_dict['figure'] = []
			for figure in figure_selectors:
				info_dict = {}
				info_dict = figure.attrs
				info_dict['text'] = figure.text.strip()
				self.parse_dict['figure'].append(info_dict)
		#extract font tags and their attributes
		font_selectors = main_soup.find_all('font')
		if font_selectors != []:
			self.parse_dict['font'] = []
			for font in font_selectors:
				info_dict = {}
				info_dict = font.attrs
				info_dict['text'] = font.text.strip()
				self.parse_dict['font'].append(info_dict)
		#extract footer tags and their attributes
		footer_selectors = main_soup.find_all('footer')
		if footer_selectors != []:
			self.parse_dict['footer'] = []
			for footer in footer_selectors:
				info_dict = {}
				info_dict = footer.attrs
				info_dict['text'] = footer.text.strip()
				self.parse_dict['footer'].append(info_dict)
		#extract form tags and their attributes
		form_selectors = main_soup.find_all('form')
		if form_selectors != []:
			self.parse_dict['form'] = []
			for form in form_selectors:
				info_dict = {}
				info_dict = form.attrs
				info_dict['text'] = form.text.strip()
				self.parse_dict['form'].append(info_dict)
		#extract frame tags and their attributes
		frame_selectors = main_soup.find_all('frame')
		if frame_selectors != []:
			self.parse_dict['frame'] = []
			for frame in frame_selectors:
				info_dict = {}
				info_dict = frame.attrs
				info_dict['text'] = frame.text.strip()
				self.parse_dict['frame'].append(info_dict)
		#extract frameset tags and their attributes
		frameset_selectors = main_soup.find_all('frameset')
		if frameset_selectors != []:
			self.parse_dict['frameset'] = []
			for frameset in frameset_selectors:
				info_dict = {}
				info_dict = frameset.attrs
				info_dict['text'] = frameset.text.strip()
				self.parse_dict['frameset'].append(info_dict)
		#extract h1 tags and their attributes
		h1_selectors = main_soup.find_all('h1')
		if h1_selectors != []:
			self.parse_dict['h1'] = []
			for h1 in h1_selectors:
				info_dict = {}
				info_dict = h1.attrs
				info_dict['text'] = h1.text.strip()
				self.parse_dict['h1'].append(info_dict)
		#extract h2 tags and their attributes
		h2_selectors = main_soup.find_all('h2')
		if h2_selectors != []:
			self.parse_dict['h2'] = []
			for h2 in h2_selectors:
				info_dict = {}
				info_dict = h2.attrs
				info_dict['text'] = h2.text.strip()
				self.parse_dict['h2'].append(info_dict)
		#extract h3 tags and their attributes
		h3_selectors = main_soup.find_all('h3')
		if h3_selectors != []:
			self.parse_dict['h3'] = []
			for h3 in h3_selectors:
				info_dict = {}
				info_dict = h3.attrs
				info_dict['text'] = h3.text.strip()
				self.parse_dict['h3'].append(info_dict)
		#extract h4 tags and their attributes
		h4_selectors = main_soup.find_all('h4')
		if h4_selectors != []:
			self.parse_dict['h4'] = []
			for h4 in h4_selectors:
				info_dict = {}
				info_dict = h4.attrs
				info_dict['text'] = h4.text.strip()
				self.parse_dict['h4'].append(info_dict)
		#extract h5 tags and their attributes
		h5_selectors = main_soup.find_all('h5')
		if h5_selectors != []:
			self.parse_dict['h5'] = []
			for h5 in h5_selectors:
				info_dict = {}
				info_dict = h5.attrs
				info_dict['text'] = h5.text.strip()
				self.parse_dict['h5'].append(info_dict)
		#extract h6 tags and their attributes
		h6_selectors = main_soup.find_all('h6')
		if h6_selectors != []:
			self.parse_dict['h6'] = []
			for h6 in h6_selectors:
				info_dict = {}
				info_dict = h6.attrs
				info_dict['text'] = h6.text.strip()
				self.parse_dict['h6'].append(info_dict)
		#extract header tags and their attributes
		header_selectors = main_soup.find_all('header')
		if header_selectors != []:
			self.parse_dict['header'] = []
			for header in header_selectors:
				info_dict = {}
				info_dict = header.attrs
				info_dict['text'] = header.text.strip()
				self.parse_dict['header'].append(info_dict)
		#extract hr tags and their attributes
		hr_selectors = main_soup.find_all('hr')
		if hr_selectors != []:
			self.parse_dict['hr'] = []
			for hr in hr_selectors:
				info_dict = {}
				info_dict = hr.attrs
				info_dict['text'] = hr.text.strip()
				self.parse_dict['hr'].append(info_dict)
		#extract i tags and their attributes
		i_selectors = main_soup.find_all('i')
		if i_selectors != []:
			self.parse_dict['i'] = []
			for i in i_selectors:
				info_dict = {}
				info_dict = i.attrs
				info_dict['text'] = i.text.strip()
				self.parse_dict['i'].append(info_dict)
		#extract iframe tags and their attributes
		iframe_selectors = main_soup.find_all('iframe')
		if iframe_selectors != []:
			self.parse_dict['iframe'] = []
			for iframe in iframe_selectors:
				info_dict = {}
				info_dict = iframe.attrs
				info_dict['text'] = iframe.text.strip()
				self.parse_dict['iframe'].append(info_dict)
		#extract img tags and their attributes
		img_selectors = main_soup.find_all('img')
		if img_selectors != []:
			self.parse_dict['img'] = []
			for img in img_selectors:
				info_dict = {}
				info_dict = img.attrs
				info_dict['text'] = img.text.strip()
				self.parse_dict['img'].append(info_dict)
		#extract input tags and their attributes
		input_selectors = main_soup.find_all('input')
		if input_selectors != []:
			self.parse_dict['input'] = []
			for input_ in input_selectors:
				info_dict = {}
				info_dict = input_.attrs
				info_dict['text'] = input_.text.strip()
				self.parse_dict['input'].append(info_dict)
		#extract ins tags and their attributes
		ins_selectors = main_soup.find_all('ins')
		if ins_selectors != []:
			self.parse_dict['ins'] = []
			for ins in ins_selectors:
				info_dict = {}
				info_dict = ins.attrs
				info_dict['text'] = ins.text.strip()
				self.parse_dict['ins'].append(info_dict)
		#extract kbd tags and their attributes
		kbd_selectors = main_soup.find_all('kbd')
		if kbd_selectors != []:
			self.parse_dict['kbd'] = []
			for kbd in kbd_selectors:
				info_dict = {}
				info_dict = kbd.attrs
				info_dict['text'] = kbd.text.strip()
				self.parse_dict['kbd'].append(info_dict)
		#extract label tags and their attributes
		label_selectors = main_soup.find_all('label')
		if label_selectors != []:
			self.parse_dict['label'] = []
			for label in label_selectors:
				info_dict = {}
				info_dict = label.attrs
				info_dict['text'] = label.text.strip()
				self.parse_dict['label'].append(info_dict)
		#extract legend tags and their attributes
		legend_selectors = main_soup.find_all('legend')
		if legend_selectors != []:
			self.parse_dict['legend'] = []
			for legend in legend_selectors:
				info_dict = {}
				info_dict = legend.attrs
				info_dict['text'] = legend.text.strip()
				self.parse_dict['legend'].append(info_dict)
		#extract li tags and their attributes
		li_selectors = main_soup.find_all('li')
		if li_selectors != []:
			self.parse_dict['li'] = []
			for li in li_selectors:
				info_dict = {}
				info_dict = li.attrs
				info_dict['text'] = li.text.strip()
				self.parse_dict['li'].append(info_dict)
		#extract link tags and their attributes
		link_selectors = main_soup.find_all('link')
		if link_selectors != []:
			self.parse_dict['link'] = []
			for link in link_selectors:
				info_dict = {}
				info_dict = link.attrs
				info_dict['text'] = link.text.strip()
				self.parse_dict['link'].append(info_dict)
		#extract main tags and their attributes
		main_selectors = main_soup.find_all('main')
		if main_selectors != []:
			self.parse_dict['main'] = []
			for main in main_selectors:
				info_dict = {}
				info_dict = main.attrs
				info_dict['text'] = main.text.strip()
				self.parse_dict['main'].append(info_dict)
		#extract map tags and their attributes
		map_selectors = main_soup.find_all('map')
		if map_selectors != []:
			self.parse_dict['map'] = []
			for map_ in map_selectors:
				info_dict = {}
				info_dict = map_.attrs
				info_dict['text'] = map_.text.strip()
				self.parse_dict['map'].append(info_dict)
		#extract mark tags and their attributes
		mark_selectors = main_soup.find_all('mark')
		if mark_selectors != []:
			self.parse_dict['mark'] = []
			for mark in mark_selectors:
				info_dict = {}
				info_dict = mark.attrs
				info_dict['text'] = mark.text.strip()
				self.parse_dict['mark'].append(info_dict)
		#extract meta tags and their attributes
		meta_selectors = main_soup.find_all('meta')
		if meta_selectors != []:
			self.parse_dict['meta'] = []
			for meta in meta_selectors:
				info_dict = {}
				info_dict = meta.attrs
				info_dict['text'] = meta.text.strip()
				self.parse_dict['meta'].append(info_dict)
		#extract meter tags and their attributes
		meter_selectors = main_soup.find_all('meter')
		if meter_selectors != []:
			self.parse_dict['meter'] = []
			for meter in meter_selectors:
				info_dict = {}
				info_dict = meter.attrs
				info_dict['text'] = meter.text.strip()
				self.parse_dict['meter'].append(info_dict)
		#extract nav tags and their attributes
		nav_selectors = main_soup.find_all('nav')
		if nav_selectors != []:
			self.parse_dict['nav'] = []
			for nav in nav_selectors:
				info_dict = {}
				info_dict = nav.attrs
				info_dict['text'] = nav.text.strip()
				self.parse_dict['nav'].append(info_dict)
		#extract noframes tags and their attributes
		noframes_selectors = main_soup.find_all('noframes')
		if noframes_selectors != []:
			self.parse_dict['noframes'] = []
			for noframes in noframes_selectors:
				info_dict = {}
				info_dict = noframes.attrs
				info_dict['text'] = noframes.text.strip()
				self.parse_dict['noframes'].append(info_dict)
		#extract noscript tags and their attributes
		noscript_selectors = main_soup.find_all('noscript')
		if noscript_selectors != []:
			self.parse_dict['noscript'] = []
			for noscript in noscript_selectors:
				info_dict = {}
				info_dict = noscript.attrs
				info_dict['text'] = noscript.text.strip()
				self.parse_dict['noscript'].append(info_dict)
		#extract object tags and their attributes
		object_selectors = main_soup.find_all('object')
		if object_selectors != []:
			self.parse_dict['object'] = []
			for object_ in object_selectors:
				info_dict = {}
				info_dict = object_.attrs
				info_dict['text'] = object_.text.strip()
				self.parse_dict['object'].append(info_dict)
		#extract ol tags and their attributes
		ol_selectors = main_soup.find_all('ol')
		if ol_selectors != []:
			self.parse_dict['ol'] = []
			for ol in ol_selectors:
				info_dict = {}
				info_dict = ol.attrs
				info_dict['text'] = ol.text.strip()
				self.parse_dict['ol'].append(info_dict)
		#extract optgroup tags and their attributes
		optgroup_selectors = main_soup.find_all('optgroup')
		if optgroup_selectors != []:
			self.parse_dict['optgroup'] = []
			for optgroup in optgroup_selectors:
				info_dict = {}
				info_dict = optgroup.attrs
				info_dict['text'] = optgroup.text.strip()
				self.parse_dict['optgroup'].append(info_dict)
		#extract option tags and their attributes
		option_selectors = main_soup.find_all('option')
		if option_selectors != []:
			self.parse_dict['option'] = []
			for option in option_selectors:
				info_dict = {}
				info_dict = option.attrs
				info_dict['text'] = option.text.strip()
				self.parse_dict['option'].append(info_dict)
		#extract output tags and their attributes
		output_selectors = main_soup.find_all('output')
		if output_selectors != []:
			self.parse_dict['output'] = []
			for output in output_selectors:
				info_dict = {}
				info_dict = output.attrs
				info_dict['text'] = output.text.strip()
				self.parse_dict['output'].append(info_dict)
		#extract p tags and their attributes
		p_selectors = main_soup.find_all('p')
		if p_selectors != []:
			self.parse_dict['p'] = []
			for p in p_selectors:
				info_dict = {}
				info_dict = p.attrs
				info_dict['text'] = p.text.strip()
				self.parse_dict['p'].append(info_dict)
		#extract param tags and their attributes
		param_selectors = main_soup.find_all('param')
		if param_selectors != []:
			self.parse_dict['param'] = []
			for param in param_selectors:
				info_dict = {}
				info_dict = param.attrs
				info_dict['text'] = param.text.strip()
				self.parse_dict['param'].append(info_dict)
		#extract picture tags and their attributes
		picture_selectors = main_soup.find_all('picture')
		if picture_selectors != []:
			self.parse_dict['picture'] = []
			for picture in picture_selectors:
				info_dict = {}
				info_dict = picture.attrs
				info_dict['text'] = picture.text.strip()
				self.parse_dict['picture'].append(info_dict)
		#extract pre tags and their attributes
		pre_selectors = main_soup.find_all('pre')
		if pre_selectors != []:
			self.parse_dict['pre'] = []
			for pre in pre_selectors:
				info_dict = {}
				info_dict = pre.attrs
				info_dict['text'] = pre.text.strip()
				self.parse_dict['pre'].append(info_dict)
		#extract progress tags and their attributes
		progress_selectors = main_soup.find_all('progress')
		if progress_selectors != []:
			self.parse_dict['progress'] = []
			for progress in progress_selectors:
				info_dict = {}
				info_dict = progress.attrs
				info_dict['text'] = progress.text.strip()
				self.parse_dict['progress'].append(info_dict)
		#extract q tags and their attributes
		q_selectors = main_soup.find_all('q')
		if q_selectors != []:
			self.parse_dict['q'] = []
			for q in q_selectors:
				info_dict = {}
				info_dict = q.attrs
				info_dict['text'] = q.text.strip()
				self.parse_dict['q'].append(info_dict)
		#extract rp tags and their attributes
		rp_selectors = main_soup.find_all('rp')
		if rp_selectors != []:
			self.parse_dict['rp'] = []
			for rp in rp_selectors:
				info_dict = {}
				info_dict = rp.attrs
				info_dict['text'] = rp.text.strip()
				self.parse_dict['rp'].append(info_dict)
		#extract rt tags and their attributes
		rt_selectors = main_soup.find_all('rt')
		if rt_selectors != []:
			self.parse_dict['rt'] = []
			for rt in rt_selectors:
				info_dict = {}
				info_dict = rt.attrs
				info_dict['text'] = rt.text.strip()
				self.parse_dict['rt'].append(info_dict)
		#extract ruby tags and their attributes
		ruby_selectors = main_soup.find_all('ruby')
		if ruby_selectors != []:
			self.parse_dict['ruby'] = []
			for ruby in ruby_selectors:
				info_dict = {}
				info_dict = ruby.attrs
				info_dict['text'] = ruby.text.strip()
				self.parse_dict['ruby'].append(info_dict)
		#extract s tags and their attributes
		s_selectors = main_soup.find_all('s')
		if s_selectors != []:
			self.parse_dict['s'] = []
			for s in s_selectors:
				info_dict = {}
				info_dict = s.attrs
				info_dict['text'] = s.text.strip()
				self.parse_dict['s'].append(info_dict)
		#extract samp tags and their attributes
		samp_selectors = main_soup.find_all('samp')
		if samp_selectors != []:
			self.parse_dict['samp'] = []
			for samp in samp_selectors:
				info_dict = {}
				info_dict = samp.attrs
				info_dict['text'] = samp.text.strip()
				self.parse_dict['samp'].append(info_dict)
		#extract script tags and their attributes
		script_selectors = main_soup.find_all('script')
		if script_selectors != []:
			self.parse_dict['script'] = []
			for script in script_selectors:
				info_dict = {}
				info_dict = script.attrs
				info_dict['text'] = script.text.strip()
				self.parse_dict['script'].append(info_dict)
		#extract section tags and their attributes
		section_selectors = main_soup.find_all('section')
		if section_selectors != []:
			self.parse_dict['section'] = []
			for section in section_selectors:
				info_dict = {}
				info_dict = section.attrs
				info_dict['text'] = section.text.strip()
				self.parse_dict['section'].append(info_dict)
		#extract select tags and their attributes
		select_selectors = main_soup.find_all('select')
		if select_selectors != []:
			self.parse_dict['select'] = []
			for select in select_selectors:
				info_dict = {}
				info_dict = select.attrs
				info_dict['text'] = select.text.strip()
				self.parse_dict['select'].append(info_dict)
		#extract small tags and their attributes
		small_selectors = main_soup.find_all('small')
		if small_selectors != []:
			self.parse_dict['small'] = []
			for small in small_selectors:
				info_dict = {}
				info_dict = small.attrs
				info_dict['text'] = small.text.strip()
				self.parse_dict['small'].append(info_dict)
		#extract source tags and their attributes
		source_selectors = main_soup.find_all('source')
		if source_selectors != []:
			self.parse_dict['source'] = []
			for source in source_selectors:
				info_dict = {}
				info_dict = source.attrs
				info_dict['text'] = source.text.strip()
				self.parse_dict['source'].append(info_dict)
		#extract span tags and their attributes
		span_selectors = main_soup.find_all('span')
		if span_selectors != []:
			self.parse_dict['span'] = []
			for span in span_selectors:
				info_dict = {}
				info_dict = span.attrs
				info_dict['text'] = span.text.strip()
				self.parse_dict['span'].append(info_dict)
		#extract strike tags and their attributes
		strike_selectors = main_soup.find_all('strike')
		if strike_selectors != []:
			self.parse_dict['strike'] = []
			for strike in strike_selectors:
				info_dict = {}
				info_dict = strike.attrs
				info_dict['text'] = strike.text.strip()
				self.parse_dict['strike'].append(info_dict)
		#extract strong tags and their attributes
		strong_selectors = main_soup.find_all('strong')
		if strong_selectors != []:
			self.parse_dict['strong'] = []
			for strong in strong_selectors:
				info_dict = {}
				info_dict = strong.attrs
				info_dict['text'] = strong.text.strip()
				self.parse_dict['strong'].append(info_dict)
		#extract style tags and their attributes
		style_selectors = main_soup.find_all('style')
		if style_selectors != []:
			self.parse_dict['style'] = []
			for style in style_selectors:
				info_dict = {}
				info_dict = style.attrs
				info_dict['text'] = style.text.strip()
				self.parse_dict['style'].append(info_dict)
		#extract sub tags and their attributes
		sub_selectors = main_soup.find_all('sub')
		if sub_selectors != []:
			self.parse_dict['sub'] = []
			for sub in sub_selectors:
				info_dict = {}
				info_dict = sub.attrs
				info_dict['text'] = sub.text.strip()
				self.parse_dict['sub'].append(info_dict)
		#extract summary tags and their attributes
		summary_selectors = main_soup.find_all('summary')
		if summary_selectors != []:
			self.parse_dict['summary'] = []
			for summary in summary_selectors:
				info_dict = {}
				info_dict = summary.attrs
				info_dict['text'] = summary.text.strip()
				self.parse_dict['summary'].append(info_dict)
		#extract sup tags and their attributes
		sup_selectors = main_soup.find_all('sup')
		if sup_selectors != []:
			self.parse_dict['sup'] = []
			for sup in sup_selectors:
				info_dict = {}
				info_dict = sup.attrs
				info_dict['text'] = sup.text.strip()
				self.parse_dict['sup'].append(info_dict)
		#extract svg tags and their attributes
		svg_selectors = main_soup.find_all('svg')
		if svg_selectors != []:
			self.parse_dict['svg'] = []
			for svg in svg_selectors:
				info_dict = {}
				info_dict = svg.attrs
				info_dict['text'] = svg.text.strip()
				self.parse_dict['svg'].append(info_dict)
		#extract table tags and their attributes
		table_selectors = main_soup.find_all('table')
		if table_selectors != []:
			self.parse_dict['table'] = []
			for table in table_selectors:
				info_dict = {}
				info_dict = table.attrs
				info_dict['text'] = table.text.strip()
				self.parse_dict['table'].append(info_dict)
		#extract tbody tags and their attributes
		tbody_selectors = main_soup.find_all('tbody')
		if tbody_selectors != []:
			self.parse_dict['tbody'] = []
			for tbody in tbody_selectors:
				info_dict = {}
				info_dict = tbody.attrs
				info_dict['text'] = tbody.text.strip()
				self.parse_dict['tbody'].append(info_dict)
		#extract td tags and their attributes
		td_selectors = main_soup.find_all('td')
		if td_selectors != []:
			self.parse_dict['td'] = []
			for td in td_selectors:
				info_dict = {}
				info_dict = td.attrs
				info_dict['text'] = td.text.strip()
				self.parse_dict['td'].append(info_dict)
		#extract template tags and their attributes
		template_selectors = main_soup.find_all('template')
		if template_selectors != []:
			self.parse_dict['template'] = []
			for template in template_selectors:
				info_dict = {}
				info_dict = template.attrs
				info_dict['text'] = template.text.strip()
				self.parse_dict['template'].append(info_dict)
		#extract textarea tags and their attributes
		textarea_selectors = main_soup.find_all('textarea')
		if textarea_selectors != []:
			self.parse_dict['textarea'] = []
			for textarea in textarea_selectors:
				info_dict = {}
				info_dict = textarea.attrs
				info_dict['text'] = textarea.text.strip()
				self.parse_dict['textarea'].append(info_dict)
		#extract tfoot tags and their attributes
		tfoot_selectors = main_soup.find_all('tfoot')
		if tfoot_selectors != []:
			self.parse_dict['tfoot'] = []
			for tfoot in tfoot_selectors:
				info_dict = {}
				info_dict = tfoot.attrs
				info_dict['text'] = tfoot.text.strip()
				self.parse_dict['tfoot'].append(info_dict)
		#extract th tags and their attributes
		th_selectors = main_soup.find_all('th')
		if th_selectors != []:
			self.parse_dict['th'] = []
			for th in th_selectors:
				info_dict = {}
				info_dict = th.attrs
				info_dict['text'] = th.text.strip()
				self.parse_dict['th'].append(info_dict)
		#extract thead tags and their attributes
		thead_selectors = main_soup.find_all('thead')
		if thead_selectors != []:
			self.parse_dict['thead'] = []
			for thead in thead_selectors:
				info_dict = {}
				info_dict = thead.attrs
				info_dict['text'] = thead.text.strip()
				self.parse_dict['thead'].append(info_dict)
		#extract time tags and their attributes
		time_selectors = main_soup.find_all('time')
		if time_selectors != []:
			self.parse_dict['time'] = []
			for time in time_selectors:
				info_dict = {}
				info_dict = time.attrs
				info_dict['text'] = time.text.strip()
				self.parse_dict['time'].append(info_dict)
		#extract title tags and their attributes
		title_selectors = main_soup.find_all('title')
		if title_selectors != []:
			self.parse_dict['title'] = []
			for title in title_selectors:
				info_dict = {}
				info_dict = title.attrs
				info_dict['text'] = title.text.strip()
				self.parse_dict['title'].append(info_dict)
		#extract tr tags and their attributes
		tr_selectors = main_soup.find_all('tr')
		if tr_selectors != []:
			self.parse_dict['tr'] = []
			for tr in tr_selectors:
				info_dict = {}
				info_dict = tr.attrs
				info_dict['text'] = tr.text.strip()
				self.parse_dict['tr'].append(info_dict)
		#extract track tags and their attributes
		track_selectors = main_soup.find_all('track')
		if track_selectors != []:
			self.parse_dict['track'] = []
			for track in track_selectors:
				info_dict = {}
				info_dict = track.attrs
				info_dict['text'] = track.text.strip()
				self.parse_dict['track'].append(info_dict)
		#extract tt tags and their attributes
		tt_selectors = main_soup.find_all('tt')
		if tt_selectors != []:
			self.parse_dict['tt'] = []
			for tt in tt_selectors:
				info_dict = {}
				info_dict = tt.attrs
				info_dict['text'] = tt.text.strip()
				self.parse_dict['tt'].append(info_dict)
		#extract u tags and their attributes
		u_selectors = main_soup.find_all('u')
		if u_selectors != []:
			self.parse_dict['u'] = []
			for u in u_selectors:
				info_dict = {}
				info_dict = u.attrs
				info_dict['text'] = u.text.strip()
				self.parse_dict['u'].append(info_dict)
		#extract ul tags and their attributes
		ul_selectors = main_soup.find_all('ul')
		if ul_selectors != []:
			self.parse_dict['ul'] = []
			for ul in ul_selectors:
				info_dict = {}
				info_dict = ul.attrs
				info_dict['text'] = ul.text.strip()
				self.parse_dict['ul'].append(info_dict)
		#extract var tags and their attributes
		var_selectors = main_soup.find_all('var')
		if var_selectors != []:
			self.parse_dict['var'] = []
			for var in var_selectors:
				info_dict = {}
				info_dict = var.attrs
				info_dict['text'] = var.text.strip()
				self.parse_dict['var'].append(info_dict)
		#extract video tags and their attributes
		video_selectors = main_soup.find_all('video')
		if video_selectors != []:
			self.parse_dict['video'] = []
			for video in video_selectors:
				info_dict = {}
				info_dict = video.attrs
				info_dict['text'] = video.text.strip()
				self.parse_dict['video'].append(info_dict)
		#extract wbr tags and their attributes
		wbr_selectors = main_soup.find_all('wbr')
		if wbr_selectors != []:
			self.parse_dict['wbr'] = []
			for wbr in wbr_selectors:
				info_dict = {}
				info_dict = wbr.attrs
				info_dict['text'] = wbr.text.strip()
				self.parse_dict['wbr'].append(info_dict)

