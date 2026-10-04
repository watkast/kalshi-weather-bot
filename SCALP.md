# Range-Scalp Bot

*Updated Sun Oct 04 13:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2317 | 1997 | 320 (3) | 1 | $-785.62 | -5.3% |
| **+10¢** | 1806 | 1452 | 354 (4) | 1 | $-581.86 | -5.1% |
| **+15¢** | 1514 | 1139 | 375 (5) | 2 | $-495.36 | -5.2% |
| **+20¢** | 1341 | 946 | 395 (9) | 2 | $-429.67 | -5.1% |
| **+10¢ (15¢ stop)** | 2863 | 2862 | 1 (1) | 1 | $-1062.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 13:30 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-04 13:30 | +20 | ETH | UP | 0.58 | open |  |
| 10-04 13:30 | +15 | ETH | UP | 0.58 | open |  |
| 10-04 13:30 | +10 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-04 13:30 | +5 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-04 13:30 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 10-04 13:30 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-04 13:30 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-04 13:30 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-04 13:30 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-04 13:25 | +10 stop | DOGE | UP | 0.71 | 0.85 | 1.16 |
| 10-04 13:25 | +15 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 10-04 13:25 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-04 13:25 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-04 13:24 | +10 stop | BNB | UP | 0.70 | 0.34 | -3.93 |
| 10-04 13:24 | +10 | BNB | UP | 0.70 | 0.82 | 0.92 |
| 10-04 13:24 | +5 | BNB | UP | 0.70 | 0.82 | 0.92 |
| 10-04 13:23 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-04 13:23 | +10 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-04 13:22 | +5 | SOL | UP | 0.70 | 0.76 | 0.33 |
| 10-04 13:22 | +10 stop | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-04 13:22 | +10 stop | SOL | UP | 0.67 | 0.52 | -1.84 |
| 10-04 13:22 | +10 stop | SOL | DOWN | 0.39 | 0.56 | 1.35 |
| 10-04 13:20 | +10 stop | ZEC | UP | 0.68 | 0.52 | -1.93 |
| 10-04 13:20 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.77 |
| 10-04 13:20 | +10 | BNB | UP | 0.66 | 0.77 | 0.77 |
| 10-04 13:20 | +5 | BNB | UP | 0.66 | 0.72 | 0.25 |
| 10-04 13:20 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-04 13:20 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-04 13:20 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 10-04 13:19 | +10 stop | XRP | UP | 0.63 | 0.40 | -2.63 |
| 10-04 13:19 | +20 | XRP | UP | 0.63 | 0.84 | 1.84 |
| 10-04 13:19 | +15 | XRP | UP | 0.63 | 0.81 | 1.53 |
| 10-04 13:19 | +10 | XRP | UP | 0.63 | 0.74 | 0.80 |
| 10-04 13:19 | +5 | XRP | UP | 0.63 | 0.74 | 0.80 |
| 10-04 13:19 | +10 stop | ZEC | UP | 0.65 | 0.48 | -2.00 |
| 10-04 13:19 | +10 | ZEC | UP | 0.65 | no | -6.62 |
| 10-04 13:19 | +5 | ZEC | UP | 0.65 | no | -6.62 |
| 10-04 13:18 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-04 13:18 | +10 | BTC | UP | 0.65 | 0.79 | 1.12 |
