# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 11:21 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 34 | 32 | 13 (41%) | 39¢ | 47% | -$0.51 | -0% |
| Silver | 17 | 16 | 5 (31%) | 33¢ | 41% | -$4.65 | -9% |
| Gold | 17 | 16 | 8 (50%) | 46¢ | 54% | $4.14 | +5% |

*Earlier half $28.23 / later half -$28.74.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 32 | 10 (31%) | -$36.61 | -27% |
| 4¢+ ← live bot | 31 | 10 (32%) | -$15.10 | -13% |
| 6¢+ | 30 | 9 (30%) | -$7.26 | -7% |
| 8¢+ | 28 | 9 (32%) | $6.50 | +8% |
| 10¢+ | 25 | 6 (24%) | -$1.30 | -2% |
| 15¢+ | 12 | 4 (33%) | $13.32 | +50% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 797 | -5.4% |
| Hyperliquid price vs Kalshi's target | 797 | -22.3% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | Open | — |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | Open | — |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 10:52:13 PM | Silver | DOWN | 7.8 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.38 |
| 9/28 10:31:35 PM | Silver | DOWN | 13.4 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 10:31:31 PM | Gold | UP | 13.5 min | 59¢ | 68% | 7¢ | ❌ Lost | -$6.07 |
| 9/28 10:16:38 PM | Silver | DOWN | 13.4 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 10:16:04 PM | Gold | UP | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
