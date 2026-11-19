# Range-Scalp Bot

*Updated Thu Nov 19 07:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64993 | 56724 | 8269 (124) | 5 | $-17479.88 | -4.3% |
| **+10¢** | 48551 | 38878 | 9673 (165) | 5 | $-16257.83 | -5.3% |
| **+15¢** | 40711 | 30278 | 10433 (210) | 6 | $-14670.43 | -5.7% |
| **+20¢** | 36255 | 25298 | 10957 (265) | 7 | $-12973.00 | -5.7% |
| **+10¢ (15¢ stop)** | 79110 | 78946 | 164 (98) | 4 | $-29075.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 07:50 | +10 stop | HYPE | DOWN | 0.57 | open |  |
| 11-19 07:49 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-19 07:47 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-19 07:47 | +10 stop | SOL | UP | 0.56 | open |  |
| 11-19 07:47 | +10 stop | ETH | UP | 0.67 | open |  |
| 11-19 07:47 | +20 | ETH | UP | 0.67 | open |  |
| 11-19 07:47 | +15 | ETH | UP | 0.67 | open |  |
| 11-19 07:47 | +10 | ETH | UP | 0.67 | open |  |
| 11-19 07:47 | +5 | ETH | UP | 0.67 | open |  |
| 11-19 07:47 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-19 07:47 | +20 | BNB | UP | 0.68 | open |  |
| 11-19 07:47 | +15 | BNB | UP | 0.68 | open |  |
| 11-19 07:47 | +10 | BNB | UP | 0.68 | open |  |
| 11-19 07:47 | +5 | BNB | UP | 0.68 | open |  |
| 11-19 07:46 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-19 07:46 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 11-19 07:46 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-19 07:46 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-19 07:46 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-19 07:46 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.72 |
| 11-19 07:46 | +20 | ZEC | UP | 0.63 | open |  |
| 11-19 07:46 | +15 | ZEC | UP | 0.62 | open |  |
| 11-19 07:46 | +10 | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-19 07:46 | +5 | ZEC | UP | 0.62 | 0.70 | 0.48 |
| 11-19 07:46 | +10 stop | BTC | UP | 0.62 | 0.79 | 1.41 |
| 11-19 07:46 | +20 | BTC | UP | 0.62 | open |  |
| 11-19 07:46 | +15 | BTC | UP | 0.62 | 0.79 | 1.41 |
| 11-19 07:46 | +10 | BTC | UP | 0.62 | 0.79 | 1.41 |
| 11-19 07:46 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 11-19 07:46 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.75 |
| 11-19 07:46 | +20 | XRP | UP | 0.62 | 0.83 | 1.79 |
| 11-19 07:46 | +15 | XRP | UP | 0.62 | 0.83 | 1.79 |
| 11-19 07:46 | +10 | XRP | UP | 0.62 | 0.73 | 0.75 |
| 11-19 07:46 | +5 | XRP | UP | 0.62 | 0.72 | 0.64 |
| 11-19 07:46 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.14 |
| 11-19 07:46 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-19 07:46 | +15 | HYPE | DOWN | 0.66 | open |  |
| 11-19 07:46 | +10 | HYPE | DOWN | 0.65 | open |  |
| 11-19 07:46 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-19 07:46 | +10 stop | NEAR | DOWN | 0.52 | 0.32 | -2.34 |
