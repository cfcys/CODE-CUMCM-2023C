function [lambda1_max,lambda2_max,lambda3_max] = Experiment(X,L,A,C,P)
%EXPERIMENT 此处显示有关此函数的摘要
%   此处显示详细说明
% lambda1 = 0;
% lambda2 = 0;
% lambda3 = 0;
Aver_max = 0;
lambda1_max = 0;
lambda2_max = 0;
lambda3_max = 0;

progressbar('1')
for lambda1 = 0.01:0.01:1
    for lambda2 = 0.01:0.01:1
        for lambda3 = 0.01:0.01:1
            sum = 0;    % 将每一组实验的最大算子给加起来
            for epoches = 1:1:100      % 进行一百组实验
                %% 已有参数的设置
%                 X = 0.15;    % 补货率的初始值设置
                beta = 0.1.*randn(7,1) + 0;        % 蒙特卡洛模拟销售的情况
%                 L = 0.0586;    % 损失率的初始设置
%                 A = [36.34131919,39.44311919,42.19331919,40.34911919,47.38371919,38.25151919,41.92971919];    % 预计的销量情况
%                 C = [7.514217752,7.306281111,7.265334588,7.435038128,7.265160312,7.215534581,7.086171692];   % 进价情况
%                 P = 0.536;    % 盈利的率的初始设置
        %         %% 三个需要确定的参数
        %         lambda1 = 0.3;
        %         lambda2 = 0.3;
        %         lambda3 = 0.3;
                %%  新的参数
                Profit = 0;   % 总共赚的钱
                Left = 0;  % 剩货的情况
                %% 模拟过程的开展
                for i = 1:1:7
                %     disp(['当前是第',num2str(i),'天：']);
                    if beta(i) < 0   % 说明货卖的少了,假设不会剩到不用进货那种程度！！！
                        str ='货卖的少了';
                        % 先进行交易
                        Sold = A(1) * (1 + beta(i));   % 已经卖出去的数量
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = Left*L + A(i) * (X - beta(i) );     
                        % 一天的交易结束 对数据进行更改
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % 价格下降
                            X = X * (1 + lambda2 * beta(i));  %  补货率下降
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % 由于价格下降，群众购买意愿在随机的基础上上升
                        end
                    elseif Left*L + A(i)*(1 + X) < A(i)*(1 +  beta(i))      % 剩下的和货物加上新进的都不满足 也即卖断货了
                        str ='买断货了';
                        % 先进行交易
                        Sold = Left + A(i)*(1 + X);   % 已经卖出去的数量
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = 0;     % 要改！！！  
                        % 一天的交易结束 对数据进行更改
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % 价格上升
                            X = X * (1 + lambda2 * beta(i));  %  补货率上升
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % 由于价格上升，群众购买意愿在随机的基础上下降
                        end
                    else     % 比预测结果好，但是没有卖断货的情况
                        str ='销量比预测结果好';
                        Sold = A(1) * (1 + beta(i));   % 已经卖出去的数量
                        Get_Single = C(i) * P;
                        Profit = Profit + Sold * Get_Single;
                        Left = Left*L + A(i) * (X - beta(i) );  
                        if i ~=7
                            P = P * (1 + lambda1 * beta(i));   % 价格上升
                            X = X * (1 + lambda2 * beta(i));  %  补货率上升
                            beta(i+1) = beta(i + 1 ) - lambda3 * beta(i);   % 由于价格上升，群众购买意愿在随机的基础上下降
                        end
                    end
                    % disp(['第',num2str(i),'天一共卖了',num2str(Sold),'间商品,今天的销售情况是',str]) 
                end
                % disp(['目前剩货:',num2str(Left),'总的收益率:',num2str(Profit)])
                sum = sum + Profit;
            end
            aver = sum / epoches;
            % disp(['在参数1=',num2str(lambda1),'在参数2=',num2str(lambda2),'在参数3=',num2str(lambda3),'的情况下,盈利的平均值为',num2str(aver)])
            if aver > Aver_max
                Aver_max = aver;
                lambda1_max = lambda1;
                lambda2_max = lambda2;
                lambda3_max = lambda3;
            end
            progressbar(lambda1/1)
        end
    end
%     progress_bar(lambda1, 0, 1);
end
disp(['经过搜索发现在参数1=',num2str(lambda1_max),'在参数2=',num2str(lambda2_max),'在参数3=',num2str(lambda3_max),'的情况下,有最佳盈利的平均值为',num2str(Aver_max)])

end

