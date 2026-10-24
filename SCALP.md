# Range-Scalp Bot

*Updated Sat Oct 24 02:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31304 | 27278 | 4026 (40) | 2 | $-9054.67 | -4.6% |
| **+10¢** | 23425 | 18775 | 4650 (58) | 2 | $-8043.95 | -5.5% |
| **+15¢** | 19603 | 14606 | 4997 (81) | 2 | $-7186.16 | -5.8% |
| **+20¢** | 17368 | 12134 | 5234 (103) | 2 | $-6417.28 | -5.9% |
| **+10¢ (15¢ stop)** | 38412 | 38353 | 59 (32) | 0 | $-14596.44 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 02:42 | +10 stop | BNB | DOWN | 0.48 | 0.93 | 4.22 |
| 10-24 02:42 | +5 | BTC | DOWN | 0.61 | 0.87 | 2.35 |
| 10-24 02:42 | +10 stop | BTC | DOWN | 0.60 | 0.87 | 2.45 |
| 10-24 02:42 | +10 stop | HYPE | UP | 0.62 | 0.91 | 2.66 |
| 10-24 02:41 | +10 stop | BNB | UP | 0.70 | 0.45 | -2.83 |
| 10-24 02:41 | +20 | BNB | UP | 0.70 | open |  |
| 10-24 02:41 | +15 | BNB | UP | 0.70 | open |  |
| 10-24 02:41 | +10 | BNB | UP | 0.70 | open |  |
| 10-24 02:41 | +5 | BNB | UP | 0.71 | open |  |
| 10-24 02:41 | +5 | NEAR | DOWN | 0.61 | 0.75 | 1.09 |
| 10-24 02:41 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 02:40 | +10 stop | BTC | UP | 0.70 | 0.53 | -2.03 |
| 10-24 02:39 | +10 stop | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 10-24 02:38 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-24 02:38 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-24 02:38 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.53 |
| 10-24 02:37 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-24 02:37 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 10-24 02:37 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-24 02:37 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-24 02:37 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-24 02:37 | +5 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-24 02:36 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-24 02:36 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 10-24 02:35 | +5 | BNB | UP | 0.62 | 0.68 | 0.29 |
| 10-24 02:33 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-24 02:33 | +10 stop | BNB | UP | 0.56 | 0.68 | 0.86 |
| 10-24 02:33 | +20 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-24 02:33 | +15 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-24 02:33 | +10 | BNB | UP | 0.56 | 0.68 | 0.86 |
| 10-24 02:33 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 10-24 02:33 | +10 stop | ETH | DOWN | 0.54 | 0.68 | 1.06 |
| 10-24 02:33 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-24 02:33 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 10-24 02:33 | +20 | SOL | DOWN | 0.71 | 0.95 | 2.21 |
| 10-24 02:33 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 10-24 02:33 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 02:33 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 02:31 | +10 stop | BTC | DOWN | 0.59 | 0.40 | -2.24 |
| 10-24 02:31 | +20 | BTC | DOWN | 0.59 | 0.87 | 2.55 |
