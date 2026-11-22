# Range-Scalp Bot

*Updated Sun Nov 22 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68153 | 59481 | 8672 (138) | 3 | $-18274.04 | -4.3% |
| **+10¢** | 50887 | 40758 | 10129 (181) | 3 | $-16931.19 | -5.3% |
| **+15¢** | 42657 | 31737 | 10920 (231) | 2 | $-15182.02 | -5.7% |
| **+20¢** | 37972 | 26495 | 11477 (289) | 4 | $-13510.97 | -5.7% |
| **+10¢ (15¢ stop)** | 82985 | 82806 | 179 (111) | 0 | $-30460.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 02:57 | +10 stop | HYPE | UP | 0.51 | 0.23 | -3.11 |
| 11-22 02:57 | +10 | HYPE | UP | 0.51 | open |  |
| 11-22 02:56 | +10 stop | ETH | UP | 0.64 | 0.44 | -2.35 |
| 11-22 02:56 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 11-22 02:56 | +10 stop | DOGE | UP | 0.55 | 0.37 | -2.15 |
| 11-22 02:56 | +10 stop | HYPE | UP | 0.47 | 0.60 | 0.95 |
| 11-22 02:55 | +10 | HYPE | UP | 0.49 | 0.60 | 0.75 |
| 11-22 02:55 | +10 stop | BNB | UP | 0.63 | 0.48 | -1.85 |
| 11-22 02:55 | +10 | HYPE | DOWN | 0.44 | 0.63 | 1.55 |
| 11-22 02:55 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-22 02:55 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 11-22 02:55 | +10 stop | NEAR | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 02:55 | +10 stop | ETH | DOWN | 0.49 | 0.31 | -2.13 |
| 11-22 02:54 | +10 stop | DOGE | DOWN | 0.60 | 0.42 | -2.15 |
| 11-22 02:54 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-22 02:54 | +10 stop | SOL | DOWN | 0.57 | 0.38 | -2.25 |
| 11-22 02:54 | +10 stop | HYPE | DOWN | 0.66 | 0.36 | -3.33 |
| 11-22 02:54 | +10 stop | DOGE | UP | 0.45 | 0.57 | 0.84 |
| 11-22 02:54 | +10 stop | XRP | UP | 0.48 | 0.63 | 1.15 |
| 11-22 02:53 | +10 stop | HYPE | UP | 0.63 | 0.43 | -2.35 |
| 11-22 02:53 | +5 | HYPE | UP | 0.63 | open |  |
| 11-22 02:53 | +10 stop | NEAR | UP | 0.54 | 0.33 | -2.44 |
| 11-22 02:52 | +10 stop | DOGE | UP | 0.59 | 0.75 | 1.29 |
| 11-22 02:52 | +10 stop | SOL | UP | 0.56 | 0.75 | 1.58 |
| 11-22 02:51 | +10 stop | ETH | UP | 0.70 | 0.48 | -2.53 |
| 11-22 02:51 | +10 stop | BNB | UP | 0.68 | 0.36 | -3.53 |
| 11-22 02:51 | +10 stop | XRP | DOWN | 0.53 | 0.36 | -2.05 |
| 11-22 02:51 | +15 | XRP | DOWN | 0.52 | 0.71 | 1.57 |
| 11-22 02:51 | +10 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-22 02:51 | +5 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-22 02:51 | +10 stop | BTC | DOWN | 0.56 | 0.70 | 1.07 |
| 11-22 02:51 | +15 | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 11-22 02:51 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-22 02:51 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-22 02:51 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-22 02:50 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-22 02:50 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 11-22 02:50 | +10 | DOGE | DOWN | 0.71 | 0.88 | 1.49 |
| 11-22 02:50 | +5 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-22 02:50 | +10 stop | DOGE | DOWN | 0.71 | 0.47 | -2.73 |
