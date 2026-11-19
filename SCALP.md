# Range-Scalp Bot

*Updated Thu Nov 19 05:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64801 | 56549 | 8252 (124) | 3 | $-17477.87 | -4.3% |
| **+10¢** | 48412 | 38759 | 9653 (165) | 3 | $-16271.25 | -5.3% |
| **+15¢** | 40597 | 30187 | 10410 (210) | 4 | $-14687.77 | -5.8% |
| **+20¢** | 36151 | 25219 | 10932 (265) | 4 | $-12993.05 | -5.7% |
| **+10¢ (15¢ stop)** | 78833 | 78669 | 164 (98) | 0 | $-28915.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 05:28 | +10 stop | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-19 05:28 | +10 | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-19 05:28 | +5 | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-19 05:24 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 11-19 05:23 | +10 stop | BTC | DOWN | 0.55 | 0.19 | -3.89 |
| 11-19 05:23 | +10 | BTC | DOWN | 0.54 | 0.67 | 0.96 |
| 11-19 05:23 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 11-19 05:23 | +10 stop | BNB | DOWN | 0.56 | 0.35 | -2.44 |
| 11-19 05:23 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-19 05:23 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-19 05:23 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-19 05:23 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-19 05:22 | +15 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 11-19 05:22 | +10 stop | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 11-19 05:22 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-19 05:22 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-19 05:21 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 11-19 05:21 | +5 | ETH | DOWN | 0.56 | 0.61 | 0.15 |
| 11-19 05:21 | +10 stop | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 11-19 05:21 | +10 stop | ETH | DOWN | 0.71 | 0.44 | -3.03 |
| 11-19 05:20 | +10 stop | XRP | UP | 0.64 | 0.84 | 1.73 |
| 11-19 05:20 | +15 | XRP | UP | 0.64 | 0.84 | 1.73 |
| 11-19 05:20 | +10 | XRP | UP | 0.64 | 0.84 | 1.73 |
| 11-19 05:20 | +5 | XRP | UP | 0.64 | 0.70 | 0.28 |
| 11-19 05:19 | +10 stop | ZEC | DOWN | 0.66 | 0.43 | -2.64 |
| 11-19 05:19 | +10 stop | DOGE | UP | 0.52 | 0.67 | 1.16 |
| 11-19 05:19 | +5 | DOGE | UP | 0.52 | 0.67 | 1.16 |
| 11-19 05:19 | +10 stop | ETH | DOWN | 0.51 | 0.66 | 1.16 |
| 11-19 05:19 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 11-19 05:19 | +15 | HYPE | UP | 0.67 | 0.92 | 2.33 |
| 11-19 05:19 | +10 | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-19 05:19 | +5 | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-19 05:18 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 05:18 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 11-19 05:18 | +10 | ZEC | UP | 0.68 | 0.81 | 1.03 |
| 11-19 05:17 | +5 | ZEC | UP | 0.70 | 0.75 | 0.21 |
| 11-19 05:17 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-19 05:17 | +20 | SOL | UP | 0.60 | 0.84 | 2.13 |
| 11-19 05:17 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-19 05:17 | +10 | SOL | UP | 0.60 | 0.74 | 1.09 |
