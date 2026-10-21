# Range-Scalp Bot

*Updated Wed Oct 21 06:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26778 | 23321 | 3457 (33) | 6 | $-7821.07 | -4.6% |
| **+10¢** | 20155 | 16161 | 3994 (48) | 8 | $-6910.61 | -5.5% |
| **+15¢** | 16874 | 12579 | 4295 (72) | 7 | $-6134.26 | -5.8% |
| **+20¢** | 14936 | 10433 | 4503 (91) | 8 | $-5515.91 | -5.9% |
| **+10¢ (15¢ stop)** | 32832 | 32779 | 53 (30) | 0 | $-12085.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 05:56 | +10 stop | ETH | UP | 0.56 | 0.20 | -3.90 |
| 10-21 05:55 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-21 05:54 | +10 stop | BNB | DOWN | 0.56 | 0.37 | -2.25 |
| 10-21 05:52 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.83 |
| 10-21 05:52 | +10 stop | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 10-21 05:52 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-21 05:51 | +10 stop | BNB | UP | 0.56 | 0.37 | -2.25 |
| 10-21 05:51 | +20 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-21 05:51 | +15 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-21 05:51 | +10 | BNB | UP | 0.58 | 0.79 | 1.80 |
| 10-21 05:51 | +5 | BNB | UP | 0.58 | 0.79 | 1.80 |
| 10-21 05:51 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 10-21 05:51 | +20 | SOL | UP | 0.54 | open |  |
| 10-21 05:51 | +15 | SOL | UP | 0.54 | open |  |
| 10-21 05:51 | +10 | SOL | UP | 0.54 | open |  |
| 10-21 05:51 | +5 | SOL | UP | 0.54 | 0.61 | 0.35 |
| 10-21 05:51 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.94 |
| 10-21 05:51 | +5 | DOGE | UP | 0.59 | open |  |
| 10-21 05:51 | +10 stop | BTC | UP | 0.66 | 0.47 | -2.24 |
| 10-21 05:51 | +20 | BTC | UP | 0.66 | open |  |
| 10-21 05:51 | +15 | BTC | UP | 0.66 | open |  |
| 10-21 05:51 | +10 | BTC | UP | 0.66 | open |  |
| 10-21 05:51 | +5 | BTC | UP | 0.66 | open |  |
| 10-21 05:51 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-21 05:51 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-21 05:51 | +15 | HYPE | DOWN | 0.64 | 0.83 | 1.59 |
| 10-21 05:51 | +5 | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-21 05:51 | +10 stop | ETH | UP | 0.67 | 0.43 | -2.74 |
| 10-21 05:51 | +20 | ETH | UP | 0.67 | open |  |
| 10-21 05:51 | +15 | ETH | UP | 0.67 | open |  |
| 10-21 05:51 | +10 | ETH | UP | 0.67 | open |  |
| 10-21 05:51 | +5 | ETH | UP | 0.67 | open |  |
| 10-21 05:50 | +10 stop | XRP | UP | 0.62 | 0.43 | -2.25 |
| 10-21 05:50 | +15 | XRP | UP | 0.62 | open |  |
| 10-21 05:50 | +10 | XRP | UP | 0.62 | open |  |
| 10-21 05:50 | +5 | XRP | UP | 0.62 | open |  |
| 10-21 05:49 | +10 stop | DOGE | UP | 0.64 | 0.38 | -2.94 |
| 10-21 05:49 | +20 | DOGE | UP | 0.64 | open |  |
| 10-21 05:49 | +15 | DOGE | UP | 0.64 | open |  |
| 10-21 05:49 | +10 | DOGE | UP | 0.64 | open |  |
