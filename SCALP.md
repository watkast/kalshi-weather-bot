# Range-Scalp Bot

*Updated Sat Nov 14 23:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59989 | 52325 | 7664 (107) | 5 | $-16350.06 | -4.3% |
| **+10¢** | 44821 | 35843 | 8978 (143) | 6 | $-15426.59 | -5.5% |
| **+15¢** | 37553 | 27873 | 9680 (180) | 6 | $-14068.80 | -6.0% |
| **+20¢** | 33457 | 23302 | 10155 (232) | 7 | $-12405.42 | -5.9% |
| **+10¢ (15¢ stop)** | 73041 | 72898 | 143 (82) | 0 | $-26869.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 23:10 | +10 stop | BTC | UP | 0.64 | 0.81 | 1.42 |
| 11-14 23:10 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 11-14 23:10 | +10 stop | SOL | UP | 0.57 | 0.80 | 2.01 |
| 11-14 23:09 | +10 stop | ETH | DOWN | 0.46 | 0.26 | -2.32 |
| 11-14 23:08 | +10 stop | BNB | UP | 0.66 | 0.43 | -2.64 |
| 11-14 23:08 | +5 | BNB | UP | 0.65 | 0.70 | 0.19 |
| 11-14 23:08 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-14 23:08 | +10 stop | SOL | UP | 0.66 | 0.41 | -2.81 |
| 11-14 23:07 | +10 stop | BTC | DOWN | 0.57 | 0.41 | -1.95 |
| 11-14 23:06 | +10 stop | ETH | DOWN | 0.66 | 0.45 | -2.44 |
| 11-14 23:06 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 11-14 23:05 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-14 23:05 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-14 23:05 | +5 | BNB | UP | 0.53 | 0.63 | 0.67 |
| 11-14 23:05 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.65 |
| 11-14 23:05 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 11-14 23:05 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 11-14 23:05 | +10 stop | SOL | UP | 0.48 | 0.59 | 0.75 |
| 11-14 23:05 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-14 23:04 | +10 stop | DOGE | UP | 0.70 | 0.53 | -2.03 |
| 11-14 23:04 | +20 | DOGE | UP | 0.70 | open |  |
| 11-14 23:04 | +15 | DOGE | UP | 0.70 | 0.87 | 1.48 |
| 11-14 23:04 | +10 | DOGE | UP | 0.70 | 0.83 | 1.06 |
| 11-14 23:04 | +5 | DOGE | UP | 0.70 | 0.77 | 0.43 |
| 11-14 23:04 | +10 stop | BNB | DOWN | 0.53 | 0.33 | -2.34 |
| 11-14 23:04 | +5 | BNB | DOWN | 0.52 | 0.60 | 0.45 |
| 11-14 23:04 | +10 stop | BTC | DOWN | 0.56 | 0.39 | -2.05 |
| 11-14 23:04 | +10 stop | SOL | DOWN | 0.61 | 0.42 | -2.25 |
| 11-14 23:03 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 11-14 23:03 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 11-14 23:03 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-14 23:03 | +10 stop | XRP | DOWN | 0.68 | 0.53 | -1.84 |
| 11-14 23:03 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-14 23:02 | +10 stop | BNB | UP | 0.60 | 0.37 | -2.64 |
| 11-14 23:02 | +20 | BNB | UP | 0.60 | 0.84 | 2.13 |
| 11-14 23:02 | +15 | BNB | UP | 0.60 | 0.84 | 2.13 |
| 11-14 23:02 | +10 | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-14 23:02 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 11-14 23:02 | +5 | ZEC | UP | 0.54 | open |  |
| 11-14 23:02 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
