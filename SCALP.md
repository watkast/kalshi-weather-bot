# Range-Scalp Bot

*Updated Wed Oct 21 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26620 | 23184 | 3436 (33) | 1 | $-7773.44 | -4.6% |
| **+10¢** | 20025 | 16058 | 3967 (48) | 3 | $-6857.20 | -5.4% |
| **+15¢** | 16761 | 12494 | 4267 (72) | 4 | $-6099.46 | -5.8% |
| **+20¢** | 14840 | 10367 | 4473 (91) | 4 | $-5466.53 | -5.9% |
| **+10¢ (15¢ stop)** | 32600 | 32547 | 53 (30) | 1 | $-11903.92 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 03:26 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 10-21 03:24 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-21 03:24 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-21 03:20 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.27 |
| 10-21 03:20 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-21 03:20 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-21 03:20 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-21 03:19 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-21 03:18 | +5 | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-21 03:17 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 03:17 | +20 | XRP | DOWN | 0.70 | 0.92 | 2.04 |
| 10-21 03:17 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-21 03:17 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 03:17 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 10-21 03:17 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-21 03:17 | +20 | BNB | UP | 0.62 | 0.93 | 2.84 |
| 10-21 03:17 | +15 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 10-21 03:17 | +10 | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-21 03:17 | +5 | BNB | UP | 0.62 | 0.70 | 0.48 |
| 10-21 03:17 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-21 03:17 | +20 | NEAR | DOWN | 0.70 | 0.93 | 2.10 |
| 10-21 03:17 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 03:17 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-21 03:17 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 10-21 03:17 | +10 stop | ETH | DOWN | 0.66 | 0.81 | 1.24 |
| 10-21 03:17 | +5 | ETH | DOWN | 0.66 | 0.81 | 1.24 |
| 10-21 03:17 | +10 stop | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-21 03:17 | +10 stop | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 10-21 03:17 | +5 | DOGE | DOWN | 0.50 | 0.56 | 0.24 |
| 10-21 03:17 | +5 | BTC | DOWN | 0.51 | 0.59 | 0.45 |
| 10-21 03:17 | +10 stop | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-21 03:17 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 10-21 03:17 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-21 03:17 | +10 | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-21 03:17 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 03:16 | +10 stop | SOL | UP | 0.45 | 0.55 | 0.64 |
| 10-21 03:16 | +20 | SOL | UP | 0.45 | open |  |
| 10-21 03:16 | +15 | SOL | UP | 0.45 | open |  |
| 10-21 03:16 | +10 | SOL | UP | 0.45 | 0.55 | 0.64 |
| 10-21 03:16 | +5 | SOL | UP | 0.45 | 0.55 | 0.64 |
