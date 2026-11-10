# Range-Scalp Bot

*Updated Tue Nov 10 07:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54362 | 47417 | 6945 (89) | 1 | $-14840.29 | -4.3% |
| **+10¢** | 40624 | 32522 | 8102 (117) | 1 | $-13777.29 | -5.4% |
| **+15¢** | 34049 | 25314 | 8735 (150) | 1 | $-12543.13 | -5.9% |
| **+20¢** | 30319 | 21156 | 9163 (198) | 1 | $-10953.86 | -5.8% |
| **+10¢ (15¢ stop)** | 66243 | 66133 | 110 (66) | 0 | $-24497.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 07:23 | +10 stop | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-10 07:23 | +10 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-10 07:22 | +10 stop | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 11-10 07:21 | +10 stop | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 11-10 07:20 | +10 stop | HYPE | DOWN | 0.55 | 0.39 | -1.95 |
| 11-10 07:19 | +5 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-10 07:18 | +10 stop | DOGE | UP | 0.71 | 0.49 | -2.53 |
| 11-10 07:18 | +10 stop | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 11-10 07:18 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 11-10 07:17 | +10 stop | HYPE | DOWN | 0.68 | 0.48 | -2.34 |
| 11-10 07:17 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-10 07:17 | +15 | HYPE | DOWN | 0.68 | open |  |
| 11-10 07:17 | +10 | HYPE | DOWN | 0.68 | open |  |
| 11-10 07:17 | +5 | HYPE | DOWN | 0.68 | open |  |
| 11-10 07:17 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 11-10 07:17 | +20 | BNB | UP | 0.63 | 0.85 | 1.94 |
| 11-10 07:17 | +15 | BNB | UP | 0.63 | 0.78 | 1.20 |
| 11-10 07:17 | +10 | BNB | UP | 0.63 | 0.76 | 1.00 |
| 11-10 07:17 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 11-10 07:17 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 11-10 07:17 | +5 | SOL | UP | 0.63 | 0.70 | 0.38 |
| 11-10 07:17 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-10 07:17 | +20 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 07:17 | +15 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 07:17 | +10 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 07:17 | +5 | ZEC | UP | 0.65 | 0.71 | 0.29 |
| 11-10 07:16 | +10 stop | DOGE | UP | 0.69 | 0.44 | -2.83 |
| 11-10 07:16 | +20 | DOGE | UP | 0.69 | 0.94 | 2.29 |
| 11-10 07:16 | +15 | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 11-10 07:16 | +10 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-10 07:16 | +5 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-10 07:16 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-10 07:16 | +20 | NEAR | UP | 0.59 | 0.88 | 2.65 |
| 11-10 07:16 | +15 | NEAR | UP | 0.59 | 0.88 | 2.65 |
| 11-10 07:16 | +10 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-10 07:16 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 11-10 07:16 | +10 stop | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-10 07:16 | +20 | BTC | UP | 0.70 | 0.92 | 1.95 |
| 11-10 07:16 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-10 07:16 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
