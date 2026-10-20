# Range-Scalp Bot

*Updated Tue Oct 20 05:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25199 | 21938 | 3261 (31) | 5 | $-7386.45 | -4.7% |
| **+10¢** | 18957 | 15190 | 3767 (46) | 7 | $-6553.55 | -5.5% |
| **+15¢** | 15865 | 11807 | 4058 (70) | 7 | $-5909.79 | -5.9% |
| **+20¢** | 14024 | 9777 | 4247 (88) | 8 | $-5307.82 | -6.0% |
| **+10¢ (15¢ stop)** | 30920 | 30868 | 52 (30) | 0 | $-11504.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 05:56 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 05:56 | +10 stop | ETH | DOWN | 0.68 | 0.93 | 2.25 |
| 10-20 05:56 | +10 | ETH | DOWN | 0.68 | 0.93 | 2.25 |
| 10-20 05:56 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
| 10-20 05:55 | +10 stop | SOL | DOWN | 0.48 | 0.66 | 1.46 |
| 10-20 05:55 | +5 | SOL | DOWN | 0.48 | 0.66 | 1.46 |
| 10-20 05:55 | +10 stop | ETH | DOWN | 0.50 | 0.66 | 1.27 |
| 10-20 05:55 | +10 | ETH | DOWN | 0.49 | 0.66 | 1.36 |
| 10-20 05:55 | +5 | ETH | DOWN | 0.51 | 0.66 | 1.16 |
| 10-20 05:52 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 05:52 | +15 | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 10-20 05:52 | +5 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 05:52 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-20 05:52 | +10 stop | NEAR | DOWN | 0.64 | 0.40 | -2.74 |
| 10-20 05:52 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-20 05:52 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 10-20 05:52 | +20 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-20 05:52 | +15 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-20 05:52 | +10 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-20 05:52 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 10-20 05:52 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 05:52 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 05:52 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 05:52 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-20 05:51 | +5 | NEAR | UP | 0.68 | open |  |
| 10-20 05:51 | +5 | ZEC | UP | 0.65 | open |  |
| 10-20 05:51 | +10 stop | BNB | UP | 0.68 | 0.44 | -2.74 |
| 10-20 05:51 | +20 | BNB | UP | 0.68 | open |  |
| 10-20 05:51 | +15 | BNB | UP | 0.68 | open |  |
| 10-20 05:51 | +10 | BNB | UP | 0.68 | open |  |
| 10-20 05:51 | +5 | BNB | UP | 0.68 | open |  |
| 10-20 05:51 | +10 stop | DOGE | UP | 0.65 | 0.41 | -2.73 |
| 10-20 05:51 | +10 | DOGE | UP | 0.65 | open |  |
| 10-20 05:51 | +5 | DOGE | UP | 0.65 | open |  |
| 10-20 05:50 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 10-20 05:50 | +15 | BTC | UP | 0.66 | open |  |
| 10-20 05:50 | +10 | BTC | UP | 0.66 | open |  |
| 10-20 05:50 | +5 | BTC | UP | 0.66 | open |  |
| 10-20 05:49 | +10 stop | SOL | UP | 0.71 | 0.50 | -2.43 |
| 10-20 05:49 | +10 | SOL | UP | 0.71 | open |  |
