# Range-Scalp Bot

*Updated Mon Oct 26 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34671 | 30271 | 4400 (43) | 0 | $-9598.48 | -4.4% |
| **+10¢** | 25950 | 20863 | 5087 (65) | 1 | $-8397.50 | -5.1% |
| **+15¢** | 21710 | 16232 | 5478 (89) | 1 | $-7513.11 | -5.5% |
| **+20¢** | 19241 | 13498 | 5743 (112) | 1 | $-6619.76 | -5.5% |
| **+10¢ (15¢ stop)** | 42454 | 42392 | 62 (33) | 0 | $-16128.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 10:24 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-26 10:24 | +10 stop | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-26 10:24 | +10 | HYPE | DOWN | 0.71 | 0.92 | 1.92 |
| 10-26 10:24 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.91 |
| 10-26 10:24 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-26 10:24 | +15 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-26 10:24 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 10:24 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-26 10:24 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 10:24 | +20 | BTC | DOWN | 0.62 | 0.92 | 2.76 |
| 10-26 10:24 | +15 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 10:24 | +10 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 10:24 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-26 10:22 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-26 10:22 | +5 | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-26 10:21 | +10 stop | DOGE | DOWN | 0.51 | 0.31 | -2.33 |
| 10-26 10:21 | +5 | DOGE | DOWN | 0.51 | 0.58 | 0.34 |
| 10-26 10:20 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-26 10:20 | +10 stop | DOGE | UP | 0.63 | 0.38 | -2.84 |
| 10-26 10:19 | +10 stop | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-26 10:19 | +15 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 10-26 10:18 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 10:18 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 10-26 10:18 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 10:18 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 10:18 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 10:18 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 10:18 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-26 10:17 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 10:17 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 10:17 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.82 |
| 10-26 10:17 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.83 |
| 10-26 10:17 | +10 stop | DOGE | DOWN | 0.56 | 0.36 | -2.35 |
| 10-26 10:17 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-26 10:17 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-26 10:17 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-26 10:17 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-26 10:17 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
