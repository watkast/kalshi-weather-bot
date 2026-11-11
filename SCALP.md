# Range-Scalp Bot

*Updated Wed Nov 11 22:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56303 | 49100 | 7203 (95) | 1 | $-15393.79 | -4.3% |
| **+10¢** | 42075 | 33669 | 8406 (125) | 1 | $-14360.20 | -5.4% |
| **+15¢** | 35281 | 26223 | 9058 (159) | 2 | $-13038.36 | -5.9% |
| **+20¢** | 31433 | 21929 | 9504 (209) | 2 | $-11393.02 | -5.8% |
| **+10¢ (15¢ stop)** | 68616 | 68495 | 121 (73) | 0 | $-25292.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 22:34 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-11 22:34 | +5 | XRP | DOWN | 0.67 | 0.82 | 1.19 |
| 11-11 22:34 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.76 |
| 11-11 22:34 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 22:34 | +5 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 22:33 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 22:33 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-11 22:33 | +15 | SOL | DOWN | 0.67 | 0.85 | 1.55 |
| 11-11 22:33 | +10 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 11-11 22:33 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-11 22:33 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 22:33 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 11-11 22:33 | +15 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 11-11 22:33 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 22:33 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 22:33 | +10 stop | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 11-11 22:33 | +20 | XRP | DOWN | 0.54 | 0.82 | 2.51 |
| 11-11 22:33 | +15 | XRP | DOWN | 0.54 | 0.82 | 2.51 |
| 11-11 22:33 | +10 | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 11-11 22:33 | +5 | XRP | DOWN | 0.54 | 0.63 | 0.55 |
| 11-11 22:33 | +10 stop | NEAR | DOWN | 0.61 | 0.79 | 1.51 |
| 11-11 22:33 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 11-11 22:33 | +15 | NEAR | DOWN | 0.61 | 0.79 | 1.51 |
| 11-11 22:33 | +10 | NEAR | DOWN | 0.61 | 0.79 | 1.51 |
| 11-11 22:33 | +5 | NEAR | DOWN | 0.61 | 0.69 | 0.48 |
| 11-11 22:33 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-11 22:33 | +20 | DOGE | DOWN | 0.71 | 0.91 | 1.81 |
| 11-11 22:33 | +15 | DOGE | DOWN | 0.71 | 0.90 | 1.69 |
| 11-11 22:33 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-11 22:33 | +5 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-11 22:33 | +5 | ZEC | UP | 0.54 | 0.60 | 0.25 |
| 11-11 22:32 | +10 stop | HYPE | DOWN | 0.66 | 0.88 | 2.01 |
| 11-11 22:31 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 22:31 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.88 |
| 11-11 22:31 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-11 22:31 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 22:31 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-11 22:31 | +10 stop | ZEC | UP | 0.50 | 0.60 | 0.65 |
| 11-11 22:31 | +20 | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +15 | ZEC | UP | 0.50 | open |  |
