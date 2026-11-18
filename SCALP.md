# Range-Scalp Bot

*Updated Wed Nov 18 07:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63798 | 55643 | 8155 (119) | 4 | $-17429.43 | -4.3% |
| **+10¢** | 47669 | 38123 | 9546 (160) | 4 | $-16354.07 | -5.5% |
| **+15¢** | 39964 | 29671 | 10293 (205) | 4 | $-14830.59 | -5.9% |
| **+20¢** | 35590 | 24786 | 10804 (260) | 5 | $-13120.07 | -5.9% |
| **+10¢ (15¢ stop)** | 77624 | 77466 | 158 (93) | 0 | $-28529.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 07:25 | +10 stop | DOGE | DOWN | 0.70 | 0.85 | 1.28 |
| 11-18 07:25 | +5 | ZEC | UP | 0.52 | 0.67 | 1.16 |
| 11-18 07:25 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-18 07:25 | +5 | BNB | DOWN | 0.71 | 0.90 | 1.68 |
| 11-18 07:24 | +10 stop | SOL | DOWN | 0.54 | 0.65 | 0.76 |
| 11-18 07:24 | +10 stop | XRP | DOWN | 0.71 | 0.53 | -2.13 |
| 11-18 07:24 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-18 07:23 | +10 stop | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-18 07:23 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-18 07:23 | +15 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-18 07:23 | +10 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-18 07:23 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-18 07:23 | +10 stop | ZEC | DOWN | 0.63 | 0.46 | -2.05 |
| 11-18 07:23 | +10 stop | DOGE | UP | 0.65 | 0.38 | -3.03 |
| 11-18 07:23 | +10 stop | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 07:23 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 11-18 07:23 | +15 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 07:23 | +10 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 07:23 | +5 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-18 07:23 | +10 stop | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-18 07:21 | +10 stop | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-18 07:18 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-18 07:17 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-18 07:17 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 07:17 | +10 stop | DOGE | DOWN | 0.67 | 0.38 | -3.23 |
| 11-18 07:16 | +5 | XRP | UP | 0.32 | 0.55 | 1.96 |
| 11-18 07:16 | +10 stop | DOGE | UP | 0.66 | 0.42 | -2.73 |
| 11-18 07:16 | +20 | DOGE | UP | 0.66 | open |  |
| 11-18 07:16 | +15 | DOGE | UP | 0.66 | open |  |
| 11-18 07:16 | +10 | DOGE | UP | 0.66 | open |  |
| 11-18 07:16 | +5 | DOGE | UP | 0.66 | open |  |
| 11-18 07:16 | +10 stop | HYPE | UP | 0.60 | 0.36 | -2.78 |
| 11-18 07:16 | +20 | HYPE | UP | 0.60 | open |  |
| 11-18 07:16 | +15 | HYPE | UP | 0.60 | open |  |
| 11-18 07:16 | +10 | HYPE | UP | 0.61 | open |  |
| 11-18 07:16 | +5 | HYPE | UP | 0.61 | open |  |
| 11-18 07:16 | +10 stop | XRP | UP | 0.60 | 0.29 | -3.42 |
| 11-18 07:16 | +20 | XRP | UP | 0.60 | 0.95 | 3.31 |
| 11-18 07:16 | +15 | XRP | UP | 0.60 | 0.95 | 3.31 |
| 11-18 07:16 | +10 | XRP | UP | 0.60 | 0.71 | 0.78 |
