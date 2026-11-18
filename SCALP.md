# Range-Scalp Bot

*Updated Wed Nov 18 18:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64371 | 56146 | 8225 (124) | 2 | $-17558.29 | -4.3% |
| **+10¢** | 48082 | 38462 | 9620 (165) | 2 | $-16385.67 | -5.4% |
| **+15¢** | 40312 | 29944 | 10368 (210) | 2 | $-14812.32 | -5.9% |
| **+20¢** | 35896 | 25014 | 10882 (265) | 2 | $-13094.35 | -5.8% |
| **+10¢ (15¢ stop)** | 78312 | 78148 | 164 (98) | 0 | $-28845.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 18:55 | +10 stop | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 11-18 18:55 | +15 | ZEC | DOWN | 0.61 | 0.79 | 1.51 |
| 11-18 18:55 | +10 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-18 18:55 | +5 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-18 18:53 | +10 stop | NEAR | UP | 0.63 | 0.82 | 1.62 |
| 11-18 18:52 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-18 18:52 | +10 | DOGE | DOWN | 0.69 | open |  |
| 11-18 18:52 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-18 18:51 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.94 |
| 11-18 18:51 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-18 18:51 | +10 stop | ZEC | UP | 0.49 | 0.21 | -3.10 |
| 11-18 18:49 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.35 |
| 11-18 18:49 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-18 18:49 | +5 | BTC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-18 18:49 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 11-18 18:49 | +15 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:49 | +10 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:49 | +5 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:48 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-18 18:48 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 11-18 18:48 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-18 18:48 | +5 | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-18 18:48 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-18 18:48 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-18 18:47 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 11-18 18:47 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-18 18:47 | +20 | ZEC | DOWN | 0.63 | 0.90 | 2.46 |
| 11-18 18:47 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:47 | +10 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:47 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-18 18:46 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-18 18:46 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 11-18 18:46 | +15 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:46 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-18 18:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-18 18:46 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.25 |
| 11-18 18:46 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-18 18:46 | +15 | DOGE | DOWN | 0.56 | open |  |
| 11-18 18:46 | +10 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-18 18:46 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.56 |
