# Range-Scalp Bot

*Updated Fri Nov 20 15:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66312 | 57867 | 8445 (128) | 1 | $-17871.57 | -4.3% |
| **+10¢** | 49514 | 39641 | 9873 (170) | 2 | $-16641.10 | -5.3% |
| **+15¢** | 41522 | 30875 | 10647 (217) | 2 | $-14980.93 | -5.8% |
| **+20¢** | 36970 | 25788 | 11182 (273) | 2 | $-13279.88 | -5.7% |
| **+10¢ (15¢ stop)** | 80764 | 80598 | 166 (100) | 0 | $-29838.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 15:07 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-20 15:06 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-20 15:04 | +10 stop | BNB | DOWN | 0.62 | 0.79 | 1.39 |
| 11-20 15:04 | +10 stop | ZEC | UP | 0.53 | 0.31 | -2.53 |
| 11-20 15:04 | +20 | ZEC | UP | 0.53 | open |  |
| 11-20 15:04 | +15 | ZEC | UP | 0.53 | open |  |
| 11-20 15:04 | +10 | ZEC | UP | 0.53 | open |  |
| 11-20 15:04 | +5 | ZEC | UP | 0.53 | open |  |
| 11-20 15:04 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 11-20 15:03 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-20 15:03 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 11-20 15:02 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 15:02 | +5 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-20 15:02 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.14 |
| 11-20 15:02 | +20 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 11-20 15:02 | +15 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-20 15:02 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-20 15:02 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-20 15:02 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 15:02 | +20 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-20 15:02 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-20 15:02 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 15:02 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-20 15:01 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-20 15:01 | +20 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 11-20 15:01 | +15 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 11-20 15:01 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-20 15:01 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-20 15:01 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 11-20 15:01 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 11-20 15:01 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 11-20 15:01 | +10 | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 11-20 15:01 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-20 15:01 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.80 |
| 11-20 15:01 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.95 |
| 11-20 15:01 | +15 | DOGE | DOWN | 0.63 | 0.82 | 1.63 |
| 11-20 15:01 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-20 15:01 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-20 15:01 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 15:01 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
