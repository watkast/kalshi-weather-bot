# Range-Scalp Bot

*Updated Mon Oct 19 03:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23416 | 20364 | 3052 (30) | 4 | $-6963.34 | -4.7% |
| **+10¢** | 17616 | 14100 | 3516 (44) | 5 | $-6184.15 | -5.6% |
| **+15¢** | 14768 | 10977 | 3791 (66) | 5 | $-5615.25 | -6.1% |
| **+20¢** | 13075 | 9110 | 3965 (84) | 5 | $-4974.39 | -6.1% |
| **+10¢ (15¢ stop)** | 28822 | 28771 | 51 (30) | 2 | $-10913.38 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 03:37 | +5 | HYPE | UP | 0.66 | open |  |
| 10-19 03:37 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-19 03:37 | +15 | BTC | UP | 0.61 | open |  |
| 10-19 03:37 | +5 | BTC | UP | 0.60 | 0.67 | 0.37 |
| 10-19 03:37 | +10 stop | ETH | UP | 0.71 | 0.53 | -2.13 |
| 10-19 03:37 | +15 | ETH | UP | 0.71 | open |  |
| 10-19 03:37 | +5 | ETH | UP | 0.71 | open |  |
| 10-19 03:36 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-19 03:35 | +5 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 10-19 03:35 | +10 stop | HYPE | UP | 0.52 | 0.62 | 0.65 |
| 10-19 03:35 | +10 stop | BTC | UP | 0.57 | 0.74 | 1.38 |
| 10-19 03:35 | +10 stop | DOGE | UP | 0.56 | 0.35 | -2.44 |
| 10-19 03:34 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-19 03:34 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 10-19 03:34 | +10 stop | ZEC | UP | 0.65 | 0.85 | 1.72 |
| 10-19 03:34 | +15 | ZEC | UP | 0.65 | 0.85 | 1.72 |
| 10-19 03:34 | +10 | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 10-19 03:34 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 10-19 03:33 | +10 stop | ETH | UP | 0.70 | 0.53 | -2.03 |
| 10-19 03:33 | +10 | ETH | UP | 0.70 | open |  |
| 10-19 03:32 | +10 stop | BTC | UP | 0.67 | 0.45 | -2.54 |
| 10-19 03:32 | +10 | BTC | UP | 0.67 | open |  |
| 10-19 03:32 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-19 03:32 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-19 03:32 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.15 |
| 10-19 03:32 | +20 | HYPE | UP | 0.63 | open |  |
| 10-19 03:32 | +15 | HYPE | UP | 0.63 | open |  |
| 10-19 03:32 | +10 | HYPE | UP | 0.63 | open |  |
| 10-19 03:32 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-19 03:32 | +10 stop | DOGE | UP | 0.68 | 0.52 | -1.94 |
| 10-19 03:32 | +20 | DOGE | UP | 0.68 | open |  |
| 10-19 03:32 | +15 | DOGE | UP | 0.68 | open |  |
| 10-19 03:32 | +10 | DOGE | UP | 0.69 | open |  |
| 10-19 03:32 | +5 | DOGE | UP | 0.69 | open |  |
| 10-19 03:32 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 10-19 03:32 | +10 stop | BNB | UP | 0.67 | 0.50 | -2.04 |
| 10-19 03:32 | +20 | BNB | UP | 0.67 | open |  |
| 10-19 03:32 | +15 | BNB | UP | 0.67 | open |  |
| 10-19 03:32 | +10 | BNB | UP | 0.67 | open |  |
| 10-19 03:32 | +5 | BNB | UP | 0.67 | open |  |
