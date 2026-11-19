# Range-Scalp Bot

*Updated Thu Nov 19 19:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65379 | 57084 | 8295 (124) | 2 | $-17407.12 | -4.2% |
| **+10¢** | 48817 | 39108 | 9709 (165) | 4 | $-16233.84 | -5.3% |
| **+15¢** | 40936 | 30463 | 10473 (211) | 4 | $-14610.08 | -5.7% |
| **+20¢** | 36453 | 25449 | 11004 (266) | 4 | $-12928.80 | -5.7% |
| **+10¢ (15¢ stop)** | 79578 | 79414 | 164 (98) | 3 | $-29283.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 19:02 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 11-19 19:02 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-19 19:02 | +15 | ETH | DOWN | 0.67 | open |  |
| 11-19 19:02 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-19 19:02 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-19 19:01 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-19 19:01 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-19 19:01 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-19 19:01 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-19 19:01 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-19 19:00 | +10 stop | NEAR | DOWN | 0.70 | 0.47 | -2.63 |
| 11-19 19:00 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-19 19:00 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-19 19:00 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-19 19:00 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-19 19:00 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-19 19:00 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-19 19:00 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-19 19:00 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-19 19:00 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-19 18:54 | +10 stop | NEAR | DOWN | 0.70 | 0.89 | 1.65 |
| 11-19 18:54 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.14 |
| 11-19 18:54 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 11-19 18:54 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 18:54 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 18:49 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.18 |
| 11-19 18:47 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-19 18:47 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-19 18:47 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-19 18:47 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-19 18:47 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-19 18:47 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 18:47 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-19 18:47 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 11-19 18:47 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 11-19 18:47 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-19 18:47 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-19 18:47 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-19 18:47 | +20 | ZEC | DOWN | 0.58 | 0.86 | 2.53 |
| 11-19 18:47 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
