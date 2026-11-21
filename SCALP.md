# Range-Scalp Bot

*Updated Sat Nov 21 01:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66879 | 58369 | 8510 (128) | 2 | $-17970.93 | -4.3% |
| **+10¢** | 49948 | 40003 | 9945 (170) | 2 | $-16691.43 | -5.3% |
| **+15¢** | 41885 | 31163 | 10722 (217) | 3 | $-14987.93 | -5.7% |
| **+20¢** | 37279 | 26013 | 11266 (274) | 4 | $-13314.32 | -5.7% |
| **+10¢ (15¢ stop)** | 81439 | 81273 | 166 (100) | 1 | $-30023.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 01:55 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 11-21 01:53 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-21 01:53 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-21 01:52 | +10 stop | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-21 01:52 | +15 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-21 01:52 | +10 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-21 01:52 | +5 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-21 01:52 | +15 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 11-21 01:52 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-21 01:52 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 11-21 01:51 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 11-21 01:51 | +5 | BTC | UP | 0.61 | open |  |
| 11-21 01:51 | +10 stop | BTC | UP | 0.59 | 0.42 | -2.05 |
| 11-21 01:51 | +10 stop | ETH | UP | 0.55 | 0.70 | 1.17 |
| 11-21 01:51 | +15 | ETH | UP | 0.55 | 0.70 | 1.17 |
| 11-21 01:51 | +10 | ETH | UP | 0.55 | 0.70 | 1.17 |
| 11-21 01:51 | +5 | ETH | UP | 0.55 | 0.64 | 0.55 |
| 11-21 01:51 | +5 | BTC | UP | 0.59 | 0.66 | 0.37 |
| 11-21 01:50 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-21 01:50 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-21 01:50 | +20 | DOGE | UP | 0.71 | open |  |
| 11-21 01:50 | +15 | DOGE | UP | 0.71 | open |  |
| 11-21 01:50 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-21 01:50 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 11-21 01:50 | +10 stop | BTC | UP | 0.50 | 0.66 | 1.26 |
| 11-21 01:50 | +5 | BTC | UP | 0.50 | 0.55 | 0.14 |
| 11-21 01:50 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-21 01:49 | +5 | BTC | DOWN | 0.35 | 0.67 | 2.88 |
| 11-21 01:49 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-21 01:48 | +5 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 11-21 01:48 | +10 stop | BNB | DOWN | 0.60 | 0.26 | -3.71 |
| 11-21 01:47 | +10 stop | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-21 01:47 | +15 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-21 01:47 | +10 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-21 01:47 | +10 stop | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 11-21 01:47 | +5 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-21 01:47 | +10 stop | ETH | UP | 0.58 | 0.43 | -1.86 |
| 11-21 01:47 | +20 | ETH | UP | 0.58 | open |  |
| 11-21 01:47 | +15 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 11-21 01:47 | +10 | ETH | UP | 0.58 | 0.68 | 0.66 |
