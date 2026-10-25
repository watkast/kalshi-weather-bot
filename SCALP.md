# Range-Scalp Bot

*Updated Sun Oct 25 20:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33669 | 29384 | 4285 (43) | 1 | $-9400.63 | -4.4% |
| **+10¢** | 25195 | 20238 | 4957 (65) | 1 | $-8295.65 | -5.2% |
| **+15¢** | 21074 | 15738 | 5336 (89) | 1 | $-7428.78 | -5.6% |
| **+20¢** | 18675 | 13088 | 5587 (111) | 2 | $-6526.22 | -5.6% |
| **+10¢ (15¢ stop)** | 41233 | 41171 | 62 (33) | 0 | $-15712.00 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 20:00 | +10 stop | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 20:00 | +20 | DOGE | DOWN | 0.58 | open |  |
| 10-25 20:00 | +15 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 20:00 | +10 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 20:00 | +5 | DOGE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-25 20:00 | +10 stop | HYPE | UP | 0.61 | 0.39 | -2.58 |
| 10-25 20:00 | +20 | HYPE | UP | 0.61 | open |  |
| 10-25 20:00 | +15 | HYPE | UP | 0.61 | open |  |
| 10-25 20:00 | +10 | HYPE | UP | 0.61 | open |  |
| 10-25 20:00 | +5 | HYPE | UP | 0.61 | open |  |
| 10-25 19:49 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-25 19:49 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-25 19:47 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 19:46 | +5 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 10-25 19:46 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 19:46 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 10-25 19:46 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-25 19:46 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 19:46 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-25 19:46 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-25 19:46 | +20 | BTC | DOWN | 0.54 | 0.74 | 1.68 |
| 10-25 19:46 | +15 | BTC | DOWN | 0.54 | 0.74 | 1.68 |
| 10-25 19:46 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-25 19:46 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 10-25 19:46 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 19:46 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-25 19:46 | +15 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-25 19:46 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 19:46 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-25 19:46 | +10 stop | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-25 19:46 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-25 19:46 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-25 19:46 | +10 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-25 19:46 | +5 | SOL | DOWN | 0.59 | 0.65 | 0.27 |
| 10-25 19:46 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 19:46 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.79 |
| 10-25 19:46 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-25 19:46 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 19:46 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-25 19:46 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
