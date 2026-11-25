# Range-Scalp Bot

*Updated Wed Nov 25 18:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71928 | 62781 | 9147 (158) | 0 | $-19154.72 | -4.2% |
| **+10¢** | 53667 | 42984 | 10683 (203) | 0 | $-17748.77 | -5.3% |
| **+15¢** | 44940 | 33432 | 11508 (260) | 0 | $-15844.45 | -5.6% |
| **+20¢** | 40014 | 27893 | 12121 (326) | 0 | $-14245.10 | -5.7% |
| **+10¢ (15¢ stop)** | 87569 | 87360 | 209 (128) | 0 | $-32121.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 18:43 | +10 stop | SOL | DOWN | 0.66 | 0.46 | -2.33 |
| 11-25 18:43 | +10 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-25 18:43 | +5 | SOL | DOWN | 0.65 | yes | -6.65 |
| 11-25 18:42 | +10 stop | SOL | DOWN | 0.47 | 0.63 | 1.25 |
| 11-25 18:42 | +10 | SOL | DOWN | 0.46 | 0.63 | 1.35 |
| 11-25 18:42 | +5 | SOL | DOWN | 0.47 | 0.63 | 1.25 |
| 11-25 18:41 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-25 18:41 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-25 18:41 | +5 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-25 18:40 | +10 stop | DOGE | DOWN | 0.47 | 0.14 | -3.57 |
| 11-25 18:40 | +10 | DOGE | DOWN | 0.47 | yes | -4.88 |
| 11-25 18:40 | +10 stop | HYPE | UP | 0.70 | 0.87 | 1.47 |
| 11-25 18:40 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 11-25 18:40 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-25 18:40 | +10 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-25 18:40 | +5 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-25 18:39 | +10 stop | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 11-25 18:39 | +10 | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 11-25 18:39 | +5 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-25 18:38 | +10 stop | DOGE | UP | 0.67 | 0.47 | -2.37 |
| 11-25 18:38 | +5 | DOGE | UP | 0.67 | 0.84 | 1.41 |
| 11-25 18:37 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-25 18:37 | +15 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-25 18:37 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-25 18:37 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-25 18:37 | +10 stop | SOL | DOWN | 0.67 | 0.47 | -2.34 |
| 11-25 18:37 | +20 | SOL | DOWN | 0.68 | yes | -6.96 |
| 11-25 18:37 | +15 | SOL | DOWN | 0.68 | yes | -6.96 |
| 11-25 18:37 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-25 18:37 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 11-25 18:37 | +10 stop | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-25 18:37 | +10 stop | DOGE | UP | 0.55 | 0.65 | 0.66 |
| 11-25 18:37 | +15 | DOGE | UP | 0.55 | 0.84 | 2.62 |
| 11-25 18:37 | +10 | DOGE | UP | 0.57 | 0.69 | 0.87 |
| 11-25 18:37 | +5 | DOGE | UP | 0.56 | 0.65 | 0.56 |
| 11-25 18:37 | +10 stop | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-25 18:37 | +20 | NEAR | UP | 0.65 | 0.87 | 1.96 |
| 11-25 18:37 | +15 | NEAR | UP | 0.65 | 0.87 | 1.96 |
| 11-25 18:37 | +10 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 11-25 18:37 | +5 | NEAR | UP | 0.66 | 0.76 | 0.71 |
