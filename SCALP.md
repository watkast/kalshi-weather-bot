# Range-Scalp Bot

*Updated Mon Oct 19 15:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24182 | 21026 | 3156 (31) | 0 | $-7221.03 | -4.7% |
| **+10¢** | 18185 | 14543 | 3642 (46) | 0 | $-6464.14 | -5.7% |
| **+15¢** | 15241 | 11319 | 3922 (69) | 0 | $-5847.08 | -6.1% |
| **+20¢** | 13492 | 9386 | 4106 (87) | 0 | $-5244.94 | -6.2% |
| **+10¢ (15¢ stop)** | 29770 | 29718 | 52 (30) | 0 | $-11319.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 15:20 | +10 stop | BTC | UP | 0.71 | 0.83 | 0.95 |
| 10-19 15:20 | +5 | BTC | UP | 0.71 | 0.83 | 0.95 |
| 10-19 15:20 | +10 stop | BNB | UP | 0.69 | 0.81 | 0.94 |
| 10-19 15:20 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-19 15:20 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-19 15:20 | +10 stop | ETH | UP | 0.61 | 0.80 | 1.61 |
| 10-19 15:19 | +10 stop | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 10-19 15:19 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 10-19 15:19 | +5 | BTC | UP | 0.61 | 0.70 | 0.58 |
| 10-19 15:19 | +10 stop | ZEC | UP | 0.61 | 0.73 | 0.84 |
| 10-19 15:18 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.68 |
| 10-19 15:18 | +5 | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 10-19 15:18 | +5 | BTC | UP | 0.52 | 0.60 | 0.45 |
| 10-19 15:18 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
| 10-19 15:18 | +15 | HYPE | UP | 0.70 | 0.86 | 1.36 |
| 10-19 15:18 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.16 |
| 10-19 15:18 | +10 | HYPE | UP | 0.69 | 0.83 | 1.16 |
| 10-19 15:18 | +5 | HYPE | UP | 0.68 | 0.83 | 1.21 |
| 10-19 15:17 | +5 | BTC | DOWN | 0.43 | 0.55 | 0.84 |
| 10-19 15:17 | +10 stop | HYPE | UP | 0.49 | 0.60 | 0.75 |
| 10-19 15:17 | +20 | HYPE | UP | 0.50 | 0.71 | 1.77 |
| 10-19 15:17 | +15 | HYPE | UP | 0.50 | 0.65 | 1.16 |
| 10-19 15:17 | +10 | HYPE | UP | 0.50 | 0.60 | 0.65 |
| 10-19 15:17 | +5 | HYPE | UP | 0.50 | 0.60 | 0.65 |
| 10-19 15:17 | +10 stop | NEAR | UP | 0.54 | 0.73 | 1.58 |
| 10-19 15:17 | +20 | NEAR | UP | 0.55 | 0.76 | 1.79 |
| 10-19 15:17 | +15 | NEAR | UP | 0.56 | 0.73 | 1.38 |
| 10-19 15:17 | +10 | NEAR | UP | 0.55 | 0.73 | 1.48 |
| 10-19 15:17 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 10-19 15:16 | +10 stop | BTC | DOWN | 0.53 | 0.29 | -2.73 |
| 10-19 15:16 | +20 | BTC | DOWN | 0.53 | yes | -5.48 |
| 10-19 15:16 | +15 | BTC | DOWN | 0.53 | yes | -5.48 |
| 10-19 15:16 | +10 | BTC | DOWN | 0.53 | yes | -5.48 |
| 10-19 15:16 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 10-19 15:16 | +5 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-19 15:16 | +5 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-19 15:16 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.85 |
| 10-19 15:16 | +20 | DOGE | DOWN | 0.61 | yes | -6.27 |
| 10-19 15:16 | +15 | DOGE | DOWN | 0.61 | yes | -6.27 |
| 10-19 15:16 | +10 | DOGE | DOWN | 0.62 | yes | -6.37 |
