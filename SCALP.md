# Range-Scalp Bot

*Updated Sat Nov 14 08:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59223 | 51673 | 7550 (107) | 0 | $-16001.30 | -4.3% |
| **+10¢** | 44244 | 35409 | 8835 (140) | 0 | $-15021.20 | -5.4% |
| **+15¢** | 37073 | 27546 | 9527 (176) | 1 | $-13663.91 | -5.9% |
| **+20¢** | 33024 | 23022 | 10002 (228) | 1 | $-12060.61 | -5.8% |
| **+10¢ (15¢ stop)** | 72072 | 71930 | 142 (82) | 0 | $-26506.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 08:30 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 08:30 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 11-14 08:30 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 11-14 08:30 | +10 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 08:30 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 11-14 08:30 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-14 08:30 | +20 | BTC | DOWN | 0.68 | 0.90 | 1.97 |
| 11-14 08:30 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 08:30 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-14 08:30 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-14 08:30 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 08:30 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-14 08:30 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-14 08:30 | +10 | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 08:30 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-14 08:27 | +10 stop | BNB | UP | 0.61 | 0.82 | 1.82 |
| 11-14 08:26 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-14 08:26 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-14 08:26 | +5 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-14 08:26 | +10 stop | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-14 08:26 | +20 | ETH | UP | 0.68 | 0.96 | 2.59 |
| 11-14 08:26 | +15 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-14 08:26 | +10 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-14 08:26 | +5 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-14 08:26 | +10 stop | BNB | DOWN | 0.71 | 0.42 | -3.23 |
| 11-14 08:25 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-14 08:24 | +10 stop | BTC | DOWN | 0.52 | 0.86 | 3.13 |
| 11-14 08:24 | +15 | BTC | DOWN | 0.52 | 0.86 | 3.13 |
| 11-14 08:24 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 11-14 08:23 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +10 stop | NEAR | UP | 0.52 | 0.32 | -2.34 |
| 11-14 08:23 | +10 | NEAR | UP | 0.52 | no | -5.38 |
| 11-14 08:23 | +5 | NEAR | UP | 0.52 | 0.61 | 0.55 |
| 11-14 08:23 | +10 stop | BNB | UP | 0.60 | 0.41 | -2.24 |
| 11-14 08:22 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 08:22 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 08:22 | +10 stop | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-14 08:22 | +20 | SOL | UP | 0.68 | 0.90 | 1.98 |
