from django.shortcuts import render

promotions = [
    {
        'title': 'Monitor Gamer',
        'price': 420.01,
        'url': 'https://a.co/d/69qlal0',
        'image': 'https://images.tcdn.com.br/img/img_prod/1314794/monitor_gamer_pcfort_t2701_165_27_led_full_hd_165hz_display_port_hdmi_dvi_vesa_2607_1_41f110c369e18c77abe42f0bfbe24480.jpg'

    },
    {
        'title': 'Monitor Gamer Curvado',
        'price': 999.99,
        'url': 'instagram.com',
        'image': 'https://aocstore.vtexassets.com/arquivos/ids/157559-800-800?v=637896528704470000&width=800&height=800&aspect=true'
    },
    {
        'title': 'Monitor Gamer Samsung',
        'price': 699.99,
        'url': 'https://example.com',
        'image': 'https://imgs.casasbahia.com.br/1519494878/1xg.jpg'
    },
    {
        'title': 'Passagem para Nova Iorque',
        'price': 911.01,
        'url': 'https://youtu.be/bsvSYyl_eII',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS73kBE1jdb8CXBzYhWcjnGZKu_gKoEILTQQw&s'
    },
    {
        'title': 'Iphone 12',
        'price': 6009.99,
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D',
        'image': 'https://s.cdnshm.com/catalog/za/t/74028067/apple-iphone-12-pro-max-512gb.jpg'
    },
    {
        'title': 'Volante Logitech G2001',
        'price': 2300.99,
        'url': 'https://youtube.com',
        'image': 'https://images.kabum.com.br/produtos/fotos/69305/volante-logitech-g29-driving-force-para-ps5-ps4-ps3-e-pc-941-000111_1644503634_original.jpg'
    },
] 

def home(request):
    return render(request, 'home.html')

def promotions_list(request):
    context = {
        'promotions': promotions,
    }
    return render(request, 'promotions/index.html', context)

def promotion_detail(request, pk):
    promotion = promotions[pk-0]
    return render(request, 'promotions/detail.html', {
        'promotion': promotion
    })