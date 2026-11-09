# Range-Scalp Bot

*Updated Mon Nov 09 06:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53401 | 46562 | 6839 (85) | 6 | $-14751.82 | -4.4% |
| **+10¢** | 39885 | 31907 | 7978 (110) | 8 | $-13760.92 | -5.5% |
| **+15¢** | 33420 | 24823 | 8597 (141) | 6 | $-12568.14 | -6.0% |
| **+20¢** | 29738 | 20724 | 9014 (186) | 6 | $-11057.42 | -5.9% |
| **+10¢ (15¢ stop)** | 65070 | 64964 | 106 (63) | 4 | $-24131.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 06:06 | +10 stop | BNB | UP | 0.46 | open |  |
| 11-09 06:05 | +20 | SOL | UP | 0.67 | open |  |
| 11-09 06:05 | +10 stop | SOL | UP | 0.65 | open |  |
| 11-09 06:04 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-09 06:04 | +10 stop | HYPE | UP | 0.54 | 0.65 | 0.72 |
| 11-09 06:04 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-09 06:04 | +10 stop | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 11-09 06:04 | +15 | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 11-09 06:04 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 11-09 06:04 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 11-09 06:04 | +5 | NEAR | UP | 0.69 | 0.75 | 0.32 |
| 11-09 06:04 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 11-09 06:04 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-09 06:03 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-09 06:03 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 11-09 06:03 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 11-09 06:03 | +10 stop | NEAR | UP | 0.52 | 0.62 | 0.65 |
| 11-09 06:03 | +5 | NEAR | UP | 0.52 | 0.59 | 0.35 |
| 11-09 06:02 | +10 stop | BTC | UP | 0.54 | 0.69 | 1.17 |
| 11-09 06:02 | +10 | BTC | UP | 0.54 | 0.69 | 1.17 |
| 11-09 06:02 | +5 | BTC | UP | 0.54 | 0.61 | 0.35 |
| 11-09 06:02 | +10 stop | BNB | DOWN | 0.60 | 0.41 | -2.24 |
| 11-09 06:02 | +20 | BNB | DOWN | 0.60 | open |  |
| 11-09 06:02 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-09 06:02 | +10 | BNB | DOWN | 0.60 | open |  |
| 11-09 06:02 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 11-09 06:02 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-09 06:02 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-09 06:02 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-09 06:02 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-09 06:02 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-09 06:01 | +10 stop | BTC | DOWN | 0.44 | 0.56 | 0.84 |
| 11-09 06:01 | +20 | BTC | DOWN | 0.44 | open |  |
| 11-09 06:01 | +15 | BTC | DOWN | 0.44 | open |  |
| 11-09 06:01 | +10 | BTC | DOWN | 0.44 | 0.56 | 0.84 |
| 11-09 06:01 | +5 | BTC | DOWN | 0.44 | 0.56 | 0.84 |
| 11-09 06:01 | +10 stop | XRP | DOWN | 0.68 | 0.50 | -2.14 |
| 11-09 06:01 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-09 06:01 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-09 06:01 | +10 | XRP | DOWN | 0.69 | open |  |
