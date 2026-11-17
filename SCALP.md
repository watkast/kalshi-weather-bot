# Range-Scalp Bot

*Updated Tue Nov 17 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62467 | 54498 | 7969 (117) | 0 | $-16913.95 | -4.3% |
| **+10¢** | 46656 | 37330 | 9326 (159) | 0 | $-15791.20 | -5.4% |
| **+15¢** | 39102 | 29042 | 10060 (201) | 0 | $-14355.80 | -5.9% |
| **+20¢** | 34851 | 24300 | 10551 (256) | 0 | $-12542.86 | -5.7% |
| **+10¢ (15¢ stop)** | 76022 | 75866 | 156 (92) | 0 | $-28011.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 00:13 | +10 stop | DOGE | DOWN | 0.71 | 0.90 | 1.68 |
| 11-17 00:12 | +10 stop | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 11-17 00:12 | +10 stop | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-17 00:12 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-17 00:12 | +10 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-17 00:12 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-17 00:12 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-17 00:12 | +20 | ZEC | DOWN | 0.66 | 0.90 | 2.17 |
| 11-17 00:12 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 00:12 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 00:12 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-17 00:12 | +10 stop | DOGE | DOWN | 0.48 | 0.64 | 1.25 |
| 11-17 00:11 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-17 00:11 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 00:11 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-17 00:11 | +5 | XRP | DOWN | 0.69 | 0.78 | 0.62 |
| 11-17 00:11 | +10 stop | DOGE | UP | 0.51 | 0.35 | -1.94 |
| 11-17 00:11 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-17 00:11 | +20 | XRP | DOWN | 0.48 | 0.73 | 2.18 |
| 11-17 00:11 | +15 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 11-17 00:11 | +10 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 11-17 00:11 | +5 | XRP | DOWN | 0.48 | 0.57 | 0.54 |
| 11-17 00:11 | +10 stop | NEAR | DOWN | 0.39 | 0.54 | 1.15 |
| 11-17 00:11 | +20 | NEAR | DOWN | 0.39 | 0.72 | 2.98 |
| 11-17 00:11 | +15 | NEAR | DOWN | 0.39 | 0.54 | 1.15 |
| 11-17 00:11 | +10 | NEAR | DOWN | 0.39 | 0.54 | 1.15 |
| 11-17 00:11 | +5 | NEAR | DOWN | 0.43 | 0.54 | 0.74 |
| 11-17 00:11 | +5 | SOL | UP | 0.71 | 0.80 | 0.63 |
| 11-17 00:10 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 11-17 00:10 | +5 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 11-17 00:09 | +10 stop | DOGE | UP | 0.55 | 0.66 | 0.79 |
| 11-17 00:09 | +20 | DOGE | UP | 0.51 | no | -5.28 |
| 11-17 00:09 | +15 | DOGE | UP | 0.57 | no | -5.88 |
| 11-17 00:09 | +10 | DOGE | UP | 0.57 | no | -5.88 |
| 11-17 00:09 | +5 | DOGE | UP | 0.57 | 0.66 | 0.56 |
| 11-17 00:09 | +10 stop | BNB | DOWN | 0.55 | 0.67 | 0.86 |
| 11-17 00:09 | +20 | BNB | DOWN | 0.55 | 0.81 | 2.31 |
| 11-17 00:09 | +15 | BNB | DOWN | 0.55 | 0.81 | 2.31 |
| 11-17 00:09 | +10 | BNB | DOWN | 0.55 | 0.67 | 0.86 |
| 11-17 00:09 | +5 | BNB | DOWN | 0.55 | 0.61 | 0.25 |
