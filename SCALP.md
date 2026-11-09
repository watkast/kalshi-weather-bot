# Range-Scalp Bot

*Updated Mon Nov 09 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53305 | 46480 | 6825 (85) | 1 | $-14708.34 | -4.4% |
| **+10¢** | 39811 | 31852 | 7959 (110) | 3 | $-13694.45 | -5.5% |
| **+15¢** | 33359 | 24783 | 8576 (141) | 3 | $-12499.52 | -6.0% |
| **+20¢** | 29680 | 20688 | 8992 (186) | 3 | $-10994.63 | -5.9% |
| **+10¢ (15¢ stop)** | 64953 | 64847 | 106 (63) | 0 | $-24112.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 04:41 | +10 stop | SOL | UP | 0.30 | 0.59 | 2.60 |
| 11-09 04:41 | +20 | SOL | UP | 0.30 | 0.59 | 2.58 |
| 11-09 04:41 | +15 | SOL | UP | 0.30 | 0.59 | 2.58 |
| 11-09 04:41 | +10 | SOL | UP | 0.30 | 0.59 | 2.58 |
| 11-09 04:41 | +5 | SOL | UP | 0.30 | 0.59 | 2.58 |
| 11-09 04:41 | +10 stop | NEAR | UP | 0.68 | 0.20 | -5.08 |
| 11-09 04:41 | +20 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-09 04:41 | +15 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-09 04:41 | +10 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-09 04:41 | +5 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-09 04:41 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 04:41 | +10 stop | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 04:41 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.11 |
| 11-09 04:41 | +15 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 04:41 | +10 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 04:41 | +5 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 04:40 | +10 stop | ZEC | UP | 0.48 | 0.23 | -2.81 |
| 11-09 04:40 | +20 | ZEC | UP | 0.48 | open |  |
| 11-09 04:40 | +15 | ZEC | UP | 0.48 | open |  |
| 11-09 04:40 | +10 | ZEC | UP | 0.49 | open |  |
| 11-09 04:40 | +5 | ZEC | UP | 0.49 | 0.57 | 0.44 |
| 11-09 04:40 | +10 stop | BTC | UP | 0.61 | 0.36 | -2.84 |
| 11-09 04:40 | +20 | BTC | UP | 0.61 | open |  |
| 11-09 04:40 | +15 | BTC | UP | 0.61 | open |  |
| 11-09 04:40 | +10 | BTC | UP | 0.61 | open |  |
| 11-09 04:40 | +5 | BTC | UP | 0.61 | open |  |
| 11-09 04:40 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.94 |
| 11-09 04:40 | +20 | HYPE | UP | 0.62 | open |  |
| 11-09 04:40 | +15 | HYPE | UP | 0.62 | open |  |
| 11-09 04:40 | +10 | HYPE | UP | 0.62 | open |  |
| 11-09 04:40 | +5 | HYPE | UP | 0.61 | 0.66 | 0.17 |
| 11-09 04:39 | +10 stop | ETH | UP | 0.53 | 0.36 | -2.05 |
| 11-09 04:38 | +10 stop | BNB | UP | 0.51 | 0.31 | -2.33 |
| 11-09 04:38 | +10 stop | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-09 04:38 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.86 |
| 11-09 04:38 | +15 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-09 04:38 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-09 04:38 | +5 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-09 04:36 | +10 stop | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-09 04:35 | +5 | BNB | DOWN | 0.58 | 0.68 | 0.66 |
