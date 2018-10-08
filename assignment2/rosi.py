import matplotlib.pyplot as plt
import numpy as np

# Host : (infected, all)
# sizes = {"eranet international limited":(5,103604),
#        "godaddy.com, llc":            (643, 59041960),
#        "key-systems gmbh":             (44, 1497176),
#        "enom, inc.":                   (246, 6875402),
#        "pdr ltd. d/b/a publicdomainregistry.com": (212, 5158744),
#        "tucows domains inc.":          (203, 10029986),
#        "paknic (private) limited":     (1, 4733),
#        "web commerce communications limited dba webnic.cc": (23, 331137),
#        "ru-center-ru":                 (109, 337296),
#        "hichina zhicheng technology ltd.":                 (103,7576711),
#        "ascio technologies, inc. danmark - filial af ascio technologies, inc. usa": (45,1592955),
#        "onlinenic, inc.":              (78,701508),
#        "regru-ru":                     (74,426805),
#        "alpnames limited":             (1,474077),
#        "instra corporation pty, ltd.": (19,145975),
#        "network solutions, llc.":      (92,7030561),
#        "r01-ru":                       (62,11838),
#        "ici - rotld":                  (77,564821),
#        "tiscalidomain-reg":            (25,626271),
#        "chengdu west dimension digital technology co., ltd.": (45,2326719)}

# hist = []
# for elem in sizes:
#     hist.append( sizes.get(elem)[0]/float(sizes.get(elem)[1]))

mu, sigma = 16., 1
s = np.random.lognormal(mu, sigma, 1500)
count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))/ (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.show()


# b = []
# for i in range(1000):
#     a = 10. + np.random.random(100)
#     b.append(np.product(a))
# b = np.array(b) / np.min(b) # scale values to be positive
# count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
# sigma = np.std(np.log(b))
# mu = np.mean(np.log(b))
# x = np.linspace(min(bins), max(bins), 10000)
# pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))

# plt.plot(x, pdf, color='r', linewidth=2)
# plt.show()

