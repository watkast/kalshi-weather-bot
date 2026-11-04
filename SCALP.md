# Range-Scalp Bot

*Updated Wed Nov 04 01:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46596 | 40578 | 6018 (72) | 4 | $-13374.87 | -4.6% |
| **+10¢** | 34801 | 27824 | 6977 (96) | 2 | $-12210.66 | -5.6% |
| **+15¢** | 29141 | 21637 | 7504 (124) | 4 | $-11147.97 | -6.1% |
| **+20¢** | 25889 | 18026 | 7863 (164) | 2 | $-9833.95 | -6.1% |
| **+10¢ (15¢ stop)** | 56816 | 56723 | 93 (56) | 0 | $-21251.87 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 01:24 | +10 stop | HYPE | DOWN | 0.61 | 0.23 | -4.10 |
| 11-04 01:24 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-04 01:23 | +10 stop | ZEC | UP | 0.53 | 0.72 | 1.57 |
| 11-04 01:23 | +20 | ZEC | UP | 0.53 | 0.86 | 3.03 |
| 11-04 01:23 | +15 | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-04 01:23 | +10 | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-04 01:23 | +5 | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-04 01:23 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-04 01:23 | +20 | ETH | UP | 0.58 | 0.87 | 2.64 |
| 11-04 01:23 | +15 | ETH | UP | 0.58 | 0.87 | 2.64 |
| 11-04 01:23 | +10 | ETH | UP | 0.58 | 0.87 | 2.61 |
| 11-04 01:23 | +5 | ETH | UP | 0.58 | 0.65 | 0.36 |
| 11-04 01:23 | +10 stop | XRP | UP | 0.56 | 0.29 | -3.03 |
| 11-04 01:22 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-04 01:22 | +10 stop | DOGE | UP | 0.69 | 0.49 | -2.33 |
| 11-04 01:22 | +5 | HYPE | DOWN | 0.49 | 0.58 | 0.50 |
| 11-04 01:22 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-04 01:22 | +5 | HYPE | DOWN | 0.47 | 0.55 | 0.42 |
| 11-04 01:21 | +10 stop | SOL | DOWN | 0.60 | 0.33 | -3.03 |
| 11-04 01:21 | +10 stop | DOGE | DOWN | 0.60 | 0.38 | -2.54 |
| 11-04 01:20 | +15 | ZEC | UP | 0.63 | 0.79 | 1.33 |
| 11-04 01:20 | +10 stop | ZEC | UP | 0.59 | 0.38 | -2.44 |
| 11-04 01:20 | +10 | ZEC | UP | 0.58 | 0.71 | 0.97 |
| 11-04 01:20 | +5 | ZEC | UP | 0.58 | 0.71 | 0.97 |
| 11-04 01:20 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 11-04 01:20 | +20 | BTC | UP | 0.61 | 0.85 | 2.14 |
| 11-04 01:20 | +15 | BTC | UP | 0.60 | 0.80 | 1.71 |
| 11-04 01:20 | +10 | BTC | UP | 0.60 | 0.74 | 1.09 |
| 11-04 01:20 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 11-04 01:20 | +5 | NEAR | UP | 0.59 | 0.71 | 0.88 |
| 11-04 01:20 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 11-04 01:20 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 11-04 01:19 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 01:19 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 11-04 01:19 | +10 stop | DOGE | DOWN | 0.61 | 0.42 | -2.25 |
| 11-04 01:19 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-04 01:19 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-04 01:19 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-04 01:19 | +10 stop | BNB | DOWN | 0.62 | 0.43 | -2.25 |
| 11-04 01:19 | +15 | BNB | DOWN | 0.62 | open |  |
