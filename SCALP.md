# Range-Scalp Bot

*Updated Fri Oct 23 19:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30833 | 26869 | 3964 (39) | 1 | $-8921.26 | -4.6% |
| **+10¢** | 23069 | 18487 | 4582 (57) | 1 | $-7936.57 | -5.5% |
| **+15¢** | 19299 | 14366 | 4933 (80) | 1 | $-7180.20 | -5.9% |
| **+20¢** | 17095 | 11931 | 5164 (103) | 1 | $-6404.22 | -6.0% |
| **+10¢ (15¢ stop)** | 37833 | 37774 | 59 (32) | 1 | $-14420.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 19:31 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-23 19:31 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-23 19:31 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-23 19:31 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-23 19:31 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-23 19:29 | +10 stop | HYPE | UP | 0.23 | 0.68 | 4.21 |
| 10-23 19:29 | +20 | HYPE | UP | 0.26 | 0.68 | 3.90 |
| 10-23 19:29 | +15 | HYPE | UP | 0.26 | 0.68 | 3.86 |
| 10-23 19:28 | +10 stop | XRP | UP | 0.53 | 0.36 | -2.05 |
| 10-23 19:28 | +10 | XRP | UP | 0.53 | no | -5.48 |
| 10-23 19:28 | +5 | XRP | UP | 0.53 | no | -5.48 |
| 10-23 19:27 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-23 19:26 | +10 stop | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-23 19:26 | +20 | SOL | UP | 0.51 | 0.71 | 1.67 |
| 10-23 19:26 | +15 | SOL | UP | 0.51 | 0.71 | 1.67 |
| 10-23 19:26 | +10 | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-23 19:26 | +5 | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-23 19:26 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-23 19:26 | +5 | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-23 19:25 | +10 stop | XRP | DOWN | 0.54 | 0.82 | 2.51 |
| 10-23 19:25 | +10 | XRP | DOWN | 0.54 | 0.82 | 2.51 |
| 10-23 19:25 | +5 | XRP | DOWN | 0.54 | 0.82 | 2.51 |
| 10-23 19:25 | +10 stop | NEAR | DOWN | 0.47 | 0.31 | -1.93 |
| 10-23 19:24 | +10 stop | DOGE | UP | 0.53 | 0.65 | 0.86 |
| 10-23 19:24 | +5 | DOGE | UP | 0.53 | 0.61 | 0.45 |
| 10-23 19:24 | +10 stop | NEAR | UP | 0.60 | 0.42 | -2.15 |
| 10-23 19:23 | +10 stop | ETH | DOWN | 0.69 | 0.43 | -2.93 |
| 10-23 19:23 | +10 stop | BTC | DOWN | 0.62 | 0.41 | -2.44 |
| 10-23 19:23 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-23 19:22 | +10 stop | NEAR | DOWN | 0.61 | 0.42 | -2.25 |
| 10-23 19:22 | +10 stop | ZEC | UP | 0.39 | 0.66 | 2.37 |
| 10-23 19:22 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 10-23 19:21 | +10 stop | ETH | DOWN | 0.59 | 0.41 | -2.14 |
| 10-23 19:21 | +15 | HYPE | UP | 0.48 | 0.64 | 1.21 |
| 10-23 19:21 | +10 stop | ZEC | UP | 0.52 | 0.62 | 0.65 |
| 10-23 19:21 | +10 stop | HYPE | UP | 0.56 | 0.35 | -2.44 |
| 10-23 19:20 | +10 stop | HYPE | DOWN | 0.33 | 0.56 | 1.96 |
| 10-23 19:19 | +10 stop | ETH | UP | 0.51 | 0.35 | -1.94 |
| 10-23 19:19 | +5 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-23 19:18 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
