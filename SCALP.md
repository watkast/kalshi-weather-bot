# Range-Scalp Bot

*Updated Tue Oct 27 23:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37209 | 32487 | 4722 (45) | 6 | $-10324.08 | -4.4% |
| **+10¢** | 27785 | 22314 | 5471 (67) | 7 | $-9220.35 | -5.3% |
| **+15¢** | 23246 | 17370 | 5876 (91) | 8 | $-8188.47 | -5.6% |
| **+20¢** | 20597 | 14449 | 6148 (116) | 8 | $-7157.17 | -5.5% |
| **+10¢ (15¢ stop)** | 45589 | 45524 | 65 (34) | 3 | $-17388.53 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 23:12 | +10 stop | SOL | UP | 0.65 | open |  |
| 10-27 23:12 | +15 | SOL | UP | 0.65 | open |  |
| 10-27 23:12 | +5 | SOL | UP | 0.65 | open |  |
| 10-27 23:12 | +10 stop | SOL | DOWN | 0.39 | 0.66 | 2.37 |
| 10-27 23:12 | +15 | SOL | DOWN | 0.40 | 0.66 | 2.27 |
| 10-27 23:12 | +5 | SOL | DOWN | 0.40 | 0.66 | 2.27 |
| 10-27 23:12 | +10 stop | BNB | UP | 0.71 | open |  |
| 10-27 23:11 | +10 stop | BNB | DOWN | 0.43 | 0.58 | 1.14 |
| 10-27 23:11 | +10 stop | ETH | UP | 0.68 | 0.80 | 0.92 |
| 10-27 23:11 | +5 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 10-27 23:11 | +10 stop | NEAR | DOWN | 0.48 | open |  |
| 10-27 23:11 | +10 stop | HYPE | DOWN | 0.44 | 0.59 | 1.15 |
| 10-27 23:10 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-27 23:10 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 23:10 | +10 stop | HYPE | DOWN | 0.51 | 0.31 | -2.33 |
| 10-27 23:10 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.43 |
| 10-27 23:10 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-27 23:10 | +10 stop | BTC | DOWN | 0.58 | 0.33 | -2.84 |
| 10-27 23:09 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 10-27 23:09 | +20 | NEAR | UP | 0.64 | open |  |
| 10-27 23:09 | +15 | NEAR | UP | 0.64 | open |  |
| 10-27 23:09 | +10 | NEAR | UP | 0.64 | open |  |
| 10-27 23:09 | +5 | NEAR | UP | 0.64 | open |  |
| 10-27 23:09 | +10 stop | BTC | UP | 0.61 | 0.39 | -2.54 |
| 10-27 23:08 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 10-27 23:08 | +10 stop | HYPE | UP | 0.63 | 0.41 | -2.54 |
| 10-27 23:08 | +10 stop | BNB | UP | 0.59 | 0.42 | -2.05 |
| 10-27 23:08 | +10 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-27 23:08 | +5 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-27 23:06 | +10 stop | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-27 23:06 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-27 23:06 | +10 stop | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-27 23:06 | +5 | BNB | UP | 0.54 | 0.63 | 0.55 |
| 10-27 23:05 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-27 23:05 | +20 | BNB | UP | 0.63 | open |  |
| 10-27 23:05 | +15 | BNB | UP | 0.63 | open |  |
| 10-27 23:05 | +10 | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-27 23:05 | +5 | BNB | UP | 0.63 | 0.70 | 0.38 |
| 10-27 23:04 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 10-27 23:04 | +10 stop | BTC | UP | 0.64 | 0.48 | -1.95 |
