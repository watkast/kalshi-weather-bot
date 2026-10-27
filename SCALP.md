# Range-Scalp Bot

*Updated Tue Oct 27 19:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37011 | 32319 | 4692 (44) | 5 | $-10252.08 | -4.4% |
| **+10¢** | 27642 | 22207 | 5435 (66) | 8 | $-9124.15 | -5.2% |
| **+15¢** | 23126 | 17292 | 5834 (90) | 8 | $-8057.04 | -5.5% |
| **+20¢** | 20495 | 14389 | 6106 (115) | 8 | $-7023.10 | -5.5% |
| **+10¢ (15¢ stop)** | 45342 | 45278 | 64 (33) | 0 | $-17270.74 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 19:49 | +10 stop | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-27 19:49 | +10 stop | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 19:49 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 19:49 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 19:49 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-27 19:49 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-27 19:49 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-27 19:48 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-27 19:48 | +10 stop | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 10-27 19:48 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 10-27 19:48 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-27 19:48 | +20 | HYPE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-27 19:48 | +15 | HYPE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-27 19:48 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.05 |
| 10-27 19:48 | +5 | HYPE | DOWN | 0.65 | 0.78 | 1.05 |
| 10-27 19:47 | +5 | DOGE | UP | 0.52 | open |  |
| 10-27 19:47 | +5 | BNB | UP | 0.66 | open |  |
| 10-27 19:47 | +10 stop | XRP | UP | 0.51 | 0.31 | -2.33 |
| 10-27 19:47 | +10 | XRP | UP | 0.51 | open |  |
| 10-27 19:47 | +5 | XRP | UP | 0.51 | 0.56 | 0.14 |
| 10-27 19:47 | +10 stop | DOGE | UP | 0.56 | 0.33 | -2.64 |
| 10-27 19:47 | +20 | DOGE | UP | 0.56 | open |  |
| 10-27 19:47 | +15 | DOGE | UP | 0.56 | open |  |
| 10-27 19:47 | +10 | DOGE | UP | 0.56 | open |  |
| 10-27 19:47 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-27 19:46 | +10 stop | NEAR | DOWN | 0.36 | 0.55 | 1.55 |
| 10-27 19:46 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 10-27 19:46 | +20 | SOL | UP | 0.68 | open |  |
| 10-27 19:46 | +15 | SOL | UP | 0.68 | open |  |
| 10-27 19:46 | +10 | SOL | UP | 0.68 | open |  |
| 10-27 19:46 | +5 | SOL | UP | 0.68 | open |  |
| 10-27 19:46 | +10 stop | ETH | UP | 0.57 | 0.38 | -2.25 |
| 10-27 19:46 | +10 stop | ZEC | UP | 0.69 | 0.44 | -2.83 |
| 10-27 19:46 | +20 | ZEC | UP | 0.69 | open |  |
| 10-27 19:46 | +15 | ZEC | UP | 0.69 | open |  |
| 10-27 19:46 | +10 | ZEC | UP | 0.69 | open |  |
| 10-27 19:46 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 10-27 19:46 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 10-27 19:46 | +20 | BNB | UP | 0.62 | open |  |
| 10-27 19:46 | +15 | BNB | UP | 0.62 | open |  |
