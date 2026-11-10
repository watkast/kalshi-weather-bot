# Range-Scalp Bot

*Updated Tue Nov 10 17:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54782 | 47786 | 6996 (91) | 1 | $-14908.41 | -4.3% |
| **+10¢** | 40938 | 32776 | 8162 (121) | 1 | $-13818.65 | -5.4% |
| **+15¢** | 34318 | 25520 | 8798 (155) | 1 | $-12563.14 | -5.8% |
| **+20¢** | 30551 | 21319 | 9232 (204) | 3 | $-10997.99 | -5.7% |
| **+10¢ (15¢ stop)** | 66745 | 66631 | 114 (70) | 0 | $-24690.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 17:16 | +10 stop | BNB | DOWN | 0.38 | 0.64 | 2.26 |
| 11-10 17:16 | +20 | BNB | DOWN | 0.38 | 0.64 | 2.26 |
| 11-10 17:16 | +15 | BNB | DOWN | 0.38 | 0.64 | 2.26 |
| 11-10 17:16 | +10 | BNB | DOWN | 0.38 | 0.64 | 2.26 |
| 11-10 17:16 | +5 | BNB | DOWN | 0.38 | 0.64 | 2.26 |
| 11-10 17:16 | +10 stop | SOL | DOWN | 0.62 | 0.47 | -1.85 |
| 11-10 17:16 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-10 17:16 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-10 17:16 | +10 | SOL | DOWN | 0.63 | open |  |
| 11-10 17:16 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-10 17:16 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.02 |
| 11-10 17:16 | +20 | HYPE | UP | 0.63 | open |  |
| 11-10 17:16 | +15 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-10 17:16 | +10 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-10 17:16 | +5 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-10 17:16 | +10 stop | NEAR | UP | 0.52 | 0.65 | 0.96 |
| 11-10 17:16 | +20 | NEAR | UP | 0.52 | open |  |
| 11-10 17:16 | +15 | NEAR | UP | 0.50 | 0.65 | 1.16 |
| 11-10 17:16 | +10 | NEAR | UP | 0.50 | 0.65 | 1.16 |
| 11-10 17:16 | +5 | NEAR | UP | 0.49 | 0.56 | 0.34 |
| 11-10 17:13 | +10 stop | ZEC | UP | 0.43 | 0.59 | 1.25 |
| 11-10 17:12 | +10 stop | NEAR | UP | 0.66 | 0.88 | 1.95 |
| 11-10 17:12 | +10 stop | BNB | DOWN | 0.57 | 0.18 | -4.19 |
| 11-10 17:12 | +10 stop | XRP | UP | 0.64 | 0.92 | 2.52 |
| 11-10 17:12 | +15 | XRP | UP | 0.63 | 0.92 | 2.62 |
| 11-10 17:12 | +10 | XRP | UP | 0.64 | 0.92 | 2.52 |
| 11-10 17:11 | +15 | XRP | UP | 0.42 | 0.58 | 1.24 |
| 11-10 17:11 | +10 | XRP | UP | 0.42 | 0.58 | 1.19 |
| 11-10 17:11 | +10 stop | BTC | UP | 0.49 | 0.59 | 0.65 |
| 11-10 17:10 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-10 17:10 | +10 stop | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 11-10 17:10 | +10 stop | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-10 17:10 | +10 stop | SOL | DOWN | 0.53 | 0.68 | 1.16 |
| 11-10 17:10 | +10 stop | XRP | UP | 0.71 | 0.40 | -3.42 |
| 11-10 17:09 | +10 stop | NEAR | DOWN | 0.64 | 0.37 | -3.04 |
| 11-10 17:09 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-10 17:08 | +5 | XRP | DOWN | 0.57 | yes | -5.88 |
| 11-10 17:08 | +10 stop | BTC | DOWN | 0.66 | 0.46 | -2.34 |
| 11-10 17:08 | +10 stop | XRP | UP | 0.45 | 0.57 | 0.84 |
| 11-10 17:08 | +15 | XRP | UP | 0.44 | 0.59 | 1.15 |
