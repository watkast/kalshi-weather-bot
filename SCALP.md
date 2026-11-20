# Range-Scalp Bot

*Updated Fri Nov 20 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65845 | 57469 | 8376 (124) | 1 | $-17695.71 | -4.3% |
| **+10¢** | 49176 | 39380 | 9796 (165) | 0 | $-16490.76 | -5.3% |
| **+15¢** | 41242 | 30676 | 10566 (211) | 1 | $-14856.71 | -5.7% |
| **+20¢** | 36719 | 25620 | 11099 (267) | 1 | $-13163.03 | -5.7% |
| **+10¢ (15¢ stop)** | 80163 | 79999 | 164 (98) | 1 | $-29520.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 04:45 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 11-20 04:45 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-20 04:45 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-20 04:45 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-20 04:43 | +5 | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-20 04:43 | +5 | XRP | UP | 0.59 | 0.67 | 0.46 |
| 11-20 04:43 | +10 stop | XRP | UP | 0.60 | 0.38 | -2.54 |
| 11-20 04:43 | +10 | XRP | UP | 0.66 | no | -6.76 |
| 11-20 04:42 | +5 | XRP | UP | 0.39 | 0.68 | 2.57 |
| 11-20 04:42 | +10 stop | XRP | UP | 0.41 | 0.68 | 2.37 |
| 11-20 04:42 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-20 04:41 | +10 stop | HYPE | DOWN | 0.55 | 0.22 | -3.57 |
| 11-20 04:41 | +20 | HYPE | DOWN | 0.54 | 0.82 | 2.51 |
| 11-20 04:41 | +15 | HYPE | DOWN | 0.54 | 0.82 | 2.51 |
| 11-20 04:41 | +10 | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-20 04:41 | +5 | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-20 04:39 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-20 04:38 | +10 stop | NEAR | DOWN | 0.52 | 0.35 | -2.04 |
| 11-20 04:36 | +10 stop | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 11-20 04:33 | +10 stop | NEAR | UP | 0.57 | 0.36 | -2.45 |
| 11-20 04:33 | +10 stop | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 11-20 04:32 | +10 stop | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-20 04:32 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-20 04:32 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-20 04:32 | +10 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-20 04:32 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-20 04:32 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-20 04:32 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 04:32 | +5 | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 04:32 | +10 stop | ZEC | UP | 0.51 | 0.35 | -1.94 |
| 11-20 04:32 | +10 stop | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 11-20 04:32 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-20 04:32 | +20 | BNB | DOWN | 0.71 | 0.93 | 1.96 |
| 11-20 04:32 | +15 | BNB | DOWN | 0.70 | 0.89 | 1.66 |
| 11-20 04:32 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.92 |
| 11-20 04:32 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.30 |
| 11-20 04:32 | +10 stop | ZEC | DOWN | 0.44 | 0.61 | 1.35 |
| 11-20 04:32 | +10 stop | NEAR | DOWN | 0.61 | 0.43 | -2.15 |
| 11-20 04:31 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 04:31 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.76 |
