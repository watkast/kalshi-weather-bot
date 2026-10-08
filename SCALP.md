# Range-Scalp Bot

*Updated Thu Oct 08 20:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7955 | 6897 | 1058 (13) | 8 | $-2469.10 | -4.9% |
| **+10¢** | 6020 | 4763 | 1257 (25) | 8 | $-2455.78 | -6.5% |
| **+15¢** | 5063 | 3740 | 1323 (37) | 8 | $-1981.48 | -6.2% |
| **+20¢** | 4522 | 3150 | 1372 (45) | 8 | $-1559.97 | -5.5% |
| **+10¢ (15¢ stop)** | 9669 | 9639 | 30 (19) | 0 | $-3580.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 20:39 | +10 stop | BTC | DOWN | 0.57 | 0.30 | -3.03 |
| 10-08 20:38 | +10 stop | BTC | UP | 0.43 | 0.59 | 1.25 |
| 10-08 20:37 | +10 stop | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-08 20:37 | +10 stop | BTC | DOWN | 0.58 | 0.42 | -1.96 |
| 10-08 20:36 | +10 stop | SOL | DOWN | 0.48 | 0.30 | -2.13 |
| 10-08 20:36 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-08 20:35 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-08 20:35 | +10 stop | NEAR | DOWN | 0.59 | 0.44 | -1.85 |
| 10-08 20:35 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.05 |
| 10-08 20:35 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.04 |
| 10-08 20:35 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-08 20:35 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-08 20:35 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-08 20:35 | +10 stop | BTC | DOWN | 0.62 | 0.46 | -1.95 |
| 10-08 20:35 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-08 20:35 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-08 20:35 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.32 |
| 10-08 20:33 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 20:31 | +10 stop | ZEC | DOWN | 0.54 | 0.28 | -2.93 |
| 10-08 20:31 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-08 20:31 | +15 | ZEC | DOWN | 0.54 | open |  |
| 10-08 20:31 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-08 20:31 | +5 | ZEC | DOWN | 0.54 | open |  |
| 10-08 20:31 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 10-08 20:31 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-08 20:31 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-08 20:31 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-08 20:31 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 10-08 20:31 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 20:31 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-08 20:31 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-08 20:31 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 20:31 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 20:31 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 20:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-08 20:31 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-08 20:31 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-08 20:31 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-08 20:31 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 10-08 20:31 | +20 | ETH | DOWN | 0.66 | open |  |
