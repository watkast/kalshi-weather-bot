# Range-Scalp Bot

*Updated Mon Oct 19 05:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23515 | 20451 | 3064 (30) | 1 | $-6981.68 | -4.7% |
| **+10¢** | 17688 | 14157 | 3531 (44) | 2 | $-6217.80 | -5.6% |
| **+15¢** | 14827 | 11022 | 3805 (66) | 3 | $-5630.66 | -6.1% |
| **+20¢** | 13126 | 9146 | 3980 (84) | 3 | $-4989.76 | -6.1% |
| **+10¢ (15¢ stop)** | 28972 | 28921 | 51 (30) | 0 | $-10994.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 05:28 | +10 stop | DOGE | UP | 0.14 | 0.54 | 3.73 |
| 10-19 05:28 | +10 | DOGE | UP | 0.14 | 0.54 | 3.73 |
| 10-19 05:28 | +5 | DOGE | UP | 0.14 | 0.54 | 3.73 |
| 10-19 05:26 | +10 stop | HYPE | UP | 0.62 | 0.85 | 2.04 |
| 10-19 05:26 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-19 05:26 | +15 | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 10-19 05:26 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-19 05:26 | +5 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-19 05:26 | +10 stop | BTC | UP | 0.55 | 0.35 | -2.34 |
| 10-19 05:26 | +5 | BTC | UP | 0.55 | 0.74 | 1.58 |
| 10-19 05:25 | +10 stop | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-19 05:25 | +5 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-19 05:25 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-19 05:25 | +20 | HYPE | UP | 0.68 | 0.91 | 2.07 |
| 10-19 05:25 | +15 | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-19 05:25 | +10 | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-19 05:25 | +5 | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-19 05:25 | +10 stop | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-19 05:24 | +10 stop | BTC | UP | 0.56 | 0.36 | -2.35 |
| 10-19 05:23 | +10 stop | ETH | UP | 0.66 | 0.48 | -2.14 |
| 10-19 05:23 | +10 stop | XRP | DOWN | 0.62 | 0.82 | 1.76 |
| 10-19 05:23 | +10 stop | NEAR | UP | 0.60 | 0.73 | 0.99 |
| 10-19 05:23 | +15 | NEAR | UP | 0.60 | 0.78 | 1.50 |
| 10-19 05:23 | +10 | NEAR | UP | 0.60 | 0.73 | 1.01 |
| 10-19 05:23 | +5 | NEAR | UP | 0.60 | 0.73 | 1.01 |
| 10-19 05:22 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-19 05:22 | +5 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-19 05:22 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 10-19 05:22 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-19 05:19 | +10 stop | XRP | DOWN | 0.67 | 0.49 | -2.14 |
| 10-19 05:19 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 10-19 05:19 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-19 05:19 | +10 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-19 05:19 | +5 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-19 05:19 | +10 stop | BTC | DOWN | 0.59 | 0.25 | -3.71 |
| 10-19 05:19 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-19 05:19 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-19 05:19 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-19 05:19 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 10-19 05:19 | +10 stop | SOL | DOWN | 0.55 | 0.37 | -2.15 |
