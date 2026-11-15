# Range-Scalp Bot

*Updated Sun Nov 15 13:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60848 | 53089 | 7759 (112) | 2 | $-16445.75 | -4.3% |
| **+10¢** | 45461 | 36363 | 9098 (150) | 2 | $-15512.80 | -5.4% |
| **+15¢** | 38075 | 28263 | 9812 (188) | 2 | $-14177.24 | -5.9% |
| **+20¢** | 33932 | 23640 | 10292 (240) | 2 | $-12462.12 | -5.9% |
| **+10¢ (15¢ stop)** | 74051 | 73900 | 151 (89) | 0 | $-27220.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:37 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-15 13:37 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 13:37 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 11-15 13:37 | +5 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-15 13:37 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 13:37 | +15 | HYPE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-15 13:37 | +10 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 13:37 | +5 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-15 13:37 | +5 | DOGE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-15 13:37 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-15 13:37 | +10 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-15 13:37 | +5 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 13:37 | +5 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 13:37 | +5 | XRP | DOWN | 0.57 | 0.76 | 1.59 |
| 11-15 13:35 | +10 stop | DOGE | DOWN | 0.71 | 0.53 | -2.11 |
| 11-15 13:34 | +10 stop | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-15 13:33 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 13:33 | +10 stop | SOL | DOWN | 0.70 | 0.54 | -1.93 |
| 11-15 13:33 | +10 stop | DOGE | DOWN | 0.69 | 0.49 | -2.33 |
| 11-15 13:33 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-15 13:33 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.50 |
| 11-15 13:32 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 11-15 13:32 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-15 13:32 | +20 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-15 13:32 | +15 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 11-15 13:32 | +10 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-15 13:32 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-15 13:32 | +10 stop | SOL | UP | 0.55 | 0.40 | -1.85 |
| 11-15 13:32 | +20 | SOL | UP | 0.55 | open |  |
| 11-15 13:32 | +15 | SOL | UP | 0.55 | open |  |
| 11-15 13:32 | +10 | SOL | UP | 0.55 | open |  |
| 11-15 13:32 | +5 | SOL | UP | 0.55 | open |  |
| 11-15 13:31 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-15 13:31 | +10 stop | XRP | DOWN | 0.67 | 0.46 | -2.44 |
| 11-15 13:31 | +10 stop | BNB | DOWN | 0.71 | 0.53 | -2.13 |
| 11-15 13:31 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.84 |
| 11-15 13:31 | +15 | BNB | DOWN | 0.71 | 0.89 | 1.58 |
| 11-15 13:31 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-15 13:31 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-15 13:31 | +10 stop | NEAR | UP | 0.51 | 0.35 | -1.94 |
