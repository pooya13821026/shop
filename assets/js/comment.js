function sendComment(blogId) {
    var comment = $('#comment').val();
    var parentId = $('#parent_id').val();
    $.get('/blog/send-comment', {
        blog_comment: comment,
        blog_id: blogId,
        parent_id: parentId,
    }).then(res => {
        $('#comment-region').html(res);
        $('#comment_id').val('');
        $('#parent_id').val('');
        if (parentId !== null && parentId !== '') {
            document.getElementById('comment-pointer').scrollIntoView({behavior: "smooth"})
        } else {
            document.getElementById('comment-region').scrollIntoView({behavior: "smooth"})
        }
    });
}

function replycomment(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_answer').scrollIntoView({behavior: "smooth"})
}

function sendcommentproduct(productlistId) {
    var comment = $('#comment').val();
    var parentId = $('#parent_id').val();
    $.get('/send-comment', {
        product_comment: comment,
        product_id: productlistId,
        parent_id: parentId,
    }).then(res => {
        $('#des_details3').html(res);
        $('#comment_id').val('');
        $('#parent_id').val('');
    })
}

function showlargeImg(img) {
    $('#main_img').attr('src', img)
}

function addProduct(productId) {
    const count = $('#qtybutton').val();
    $.get('/order/add-product-order?product_id=' + productId + '&count=' + count).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: 'عملیات موفق',
                text: "محصول مورد نظر به سبد خرید شما اضافه شد.",
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'تسویه حساب'
            }).then((result) => {
                if (result.isConfirmed && res.status === 'success') {
                    window.location.href = '/dashbord/user-cart'
                }
            })
        } else if (res.status === 'not_login') {
            Swal.fire({
                title: 'عملیات ناموفق',
                text: "برای خرید محصول باید وارد سایت شوید.",
                icon: 'warning',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'ورود به سایت'
            }).then((result) => {
                if (result.isConfirmed && res.status === 'not_login') {
                    window.location.href = '/login'
                }
            })
        } else if (res.status === 'product_not_found') {
            Swal.fire({
                title: 'عملیات ناموفق',
                text: "محصول مورد نظر یافت نشد",
                icon: 'error',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'رفتن به فروشگاه'
            }).then((result) => {

            })
        }
    })

}

function deleteFromOrderItems(itemId) {
    $.get('/dashbord/delete-order-item?detail_id=' + itemId).then(res => {
        if (res.status === 'success') {
            $('#item-content').html(res.data);
        }
    })
}


function changeItemCount(itemId, position) {
    console.log(itemId, position)
    $.get('/dashbord/change_item_count?detail_id=' + itemId + '&position=' + position).then(res => {
        if (res.status === 'success') {
            $('#item-content').html(res.data);
        }
    });
}
