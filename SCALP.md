# Range-Scalp Bot

*Updated Tue Oct 27 17:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36846 | 32171 | 4675 (44) | 4 | $-10228.63 | -4.4% |
| **+10¢** | 27525 | 22111 | 5414 (66) | 4 | $-9097.07 | -5.3% |
| **+15¢** | 23028 | 17218 | 5810 (90) | 6 | $-8029.52 | -5.6% |
| **+20¢** | 20408 | 14327 | 6081 (115) | 6 | $-7002.11 | -5.5% |
| **+10¢ (15¢ stop)** | 45152 | 45088 | 64 (33) | 2 | $-17219.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 17:37 | +15 | XRP | DOWN | 0.54 | 0.71 | 1.38 |
| 10-27 17:37 | +5 | XRP | DOWN | 0.54 | 0.68 | 1.07 |
| 10-27 17:37 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 17:37 | +5 | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 17:37 | +10 stop | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-27 17:37 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 10-27 17:36 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-27 17:36 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-27 17:36 | +10 | NEAR | DOWN | 0.68 | 0.82 | 1.13 |
| 10-27 17:36 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 17:36 | +10 stop | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-27 17:35 | +10 stop | SOL | DOWN | 0.56 | open |  |
| 10-27 17:35 | +5 | BNB | DOWN | 0.55 | open |  |
| 10-27 17:34 | +5 | BNB | UP | 0.51 | 0.58 | 0.34 |
| 10-27 17:34 | +5 | BTC | UP | 0.54 | open |  |
| 10-27 17:34 | +10 stop | ETH | UP | 0.56 | 0.41 | -1.85 |
| 10-27 17:34 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 17:33 | +10 stop | XRP | DOWN | 0.60 | 0.44 | -1.95 |
| 10-27 17:33 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-27 17:33 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 10-27 17:33 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 10-27 17:33 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 10-27 17:32 | +10 | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 17:32 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 10-27 17:32 | +10 stop | BNB | UP | 0.52 | open |  |
| 10-27 17:32 | +20 | BNB | UP | 0.52 | open |  |
| 10-27 17:32 | +15 | BNB | UP | 0.52 | open |  |
| 10-27 17:32 | +10 | BNB | UP | 0.52 | open |  |
| 10-27 17:32 | +5 | BNB | UP | 0.52 | 0.60 | 0.45 |
| 10-27 17:32 | +10 stop | BTC | UP | 0.54 | 0.38 | -1.95 |
| 10-27 17:32 | +20 | BTC | UP | 0.54 | open |  |
| 10-27 17:32 | +15 | BTC | UP | 0.54 | open |  |
| 10-27 17:32 | +10 | BTC | UP | 0.54 | open |  |
| 10-27 17:32 | +5 | BTC | UP | 0.54 | 0.63 | 0.55 |
| 10-27 17:32 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 17:32 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-27 17:32 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-27 17:31 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.95 |
| 10-27 17:31 | +20 | HYPE | UP | 0.54 | open |  |
| 10-27 17:31 | +15 | HYPE | UP | 0.54 | open |  |
