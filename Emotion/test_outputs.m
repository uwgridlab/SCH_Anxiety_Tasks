%setup
tbl = readtable('_EmotionTask_2021_Jan_11_1659.csv');
Num = tbl.Num;
Num(isnan(Num)) = [];
blk = tbl.blocks_thisN(~isnan(tbl.blocks_thisN));
Category = tbl.Category(~cellfun(@isempty, tbl.Category));
fprintf('Detected %d pictures in %d categories\n', length(unique(Num)), ...
    length(unique(Category)));
fprintf('Total of %d trials over %d blocks\n\n', length(Num), length(unique(blk)));
errorthrown = false;

% all pictures are used equal numbers of times overall
[~, ~, c] = unique(Num); 
ov_ct = accumarray(c, 1);
if length(unique(ov_ct)) ~= 1
    fprintf('~~Error: not all pictures used equally overall. Expected %d uses per picture and got \n',...
        length(Num)/length(unique(Num)));
    errorthrown = true;
else
    fprintf('All pictures used %d times overall\n', unique(ov_ct))
    if unique(ov_ct) ~= length(Num)/length(unique(Num))
        fprintf('~~Error: unexpected number of repetitions of each picture\n')
        errorthrown = true;
    else
        fprintf('Expected number of repetitions of each picture found\n');
    end
end

% all categories are represented equally in each block
blk_ct = zeros(length(unique(Category)), length(unique(blk)));
b = unique(blk);
for ii = 1:length(b)
    subs = Category(blk == b(ii));
    [~, ~, c] = unique(subs);
    blk_ct(:, ii) = accumarray(c, 1);
end
if length(unique(blk_ct)) ~= 1
    fprintf('~~Error: not all categories used equally in each block. Expected %d uses per block, found\n', ...
        length(Num)/length(b)/length(unique(Category)));
    errorthrown = true;
    disp(blk_ct);
    if length(unique(sum(blk_ct, 2))) ~= 1
        fprintf('~~Error: not all categories used equally overall Expected %d uses each, found\n', ...
            length(Num)/length(unique(Category)));
        disp(sum(blk_ct, 2));
        errorthrown = true;
    else
        fprintf('At least all categories are used equally overall!\n');
        if unique(sum(blk_ct, 2)) ~= length(Num)/length(b)/length(unique(Category))
            fprintf('~~Something is funky though... expected %d uses each and found %d\n', ...
                length(Num)/length(b)/length(unique(Category)), unique(sum(blk_ct, 2)))
            errorthrown = true;
        else
            fprintf('Expected number of repetitions found\n\n')
        end
    end
else
    fprintf('All categories used %d times per block\n', unique(blk_ct))
    if unique(blk_ct) ~= length(Num)/length(b)/length(unique(Category))
        fprintf('~~Error: unexpected number of items of each category in each block. Expected %d \n\n', ...
            length(Num)/length(b)/length(unique(Category)));
        errorthrown = true;
    else
        fprintf('Expected number of each category in each block\n\n');
    end
end

if ~errorthrown
    fprintf('No errors thrown!\n\n')
else
    fprintf('Errors thrown :(\n\n')
end