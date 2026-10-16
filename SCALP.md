# Range-Scalp Bot

*Updated Fri Oct 16 19:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19693 | 17115 | 2578 (29) | 0 | $-5907.68 | -4.8% |
| **+10¢** | 14849 | 11870 | 2979 (41) | 0 | $-5319.12 | -5.7% |
| **+15¢** | 12424 | 9220 | 3204 (60) | 0 | $-4812.61 | -6.2% |
| **+20¢** | 11021 | 7666 | 3355 (79) | 0 | $-4261.62 | -6.2% |
| **+10¢ (15¢ stop)** | 24239 | 24189 | 50 (29) | 0 | $-9308.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 19:12 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 10-16 19:12 | +10 stop | HYPE | UP | 0.50 | 0.61 | 0.75 |
| 10-16 19:12 | +5 | HYPE | UP | 0.50 | 0.57 | 0.34 |
| 10-16 19:11 | +10 stop | XRP | UP | 0.48 | 0.59 | 0.70 |
| 10-16 19:11 | +5 | XRP | UP | 0.48 | 0.59 | 0.75 |
| 10-16 19:11 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-16 19:11 | +5 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-16 19:11 | +10 stop | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-16 19:11 | +20 | SOL | DOWN | 0.68 | yes | -6.96 |
| 10-16 19:11 | +15 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-16 19:10 | +10 stop | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 19:10 | +20 | ZEC | DOWN | 0.65 | 0.91 | 2.37 |
| 10-16 19:10 | +15 | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 19:10 | +10 | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 19:10 | +5 | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 19:10 | +10 stop | NEAR | DOWN | 0.51 | 0.63 | 0.85 |
| 10-16 19:10 | +10 stop | BNB | UP | 0.51 | 0.68 | 1.39 |
| 10-16 19:09 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-16 19:09 | +20 | XRP | DOWN | 0.66 | yes | -6.76 |
| 10-16 19:09 | +15 | XRP | DOWN | 0.65 | yes | -6.66 |
| 10-16 19:09 | +10 | XRP | DOWN | 0.65 | yes | -6.66 |
| 10-16 19:09 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 10-16 19:09 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-16 19:09 | +5 | ETH | UP | 0.58 | 0.66 | 0.46 |
| 10-16 19:09 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-16 19:09 | +20 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:09 | +15 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:09 | +10 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:09 | +5 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:08 | +10 stop | BNB | DOWN | 0.55 | 0.33 | -2.54 |
| 10-16 19:08 | +20 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:08 | +15 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:08 | +10 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:08 | +5 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-16 19:07 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-16 19:06 | +10 stop | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-16 19:06 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-16 19:06 | +10 stop | HYPE | DOWN | 0.66 | 0.86 | 1.74 |
| 10-16 19:04 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 10-16 19:04 | +10 stop | HYPE | DOWN | 0.60 | 0.76 | 1.26 |
