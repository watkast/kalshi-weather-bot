# Range-Scalp Bot

*Updated Thu Nov 05 17:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48612 | 42367 | 6245 (73) | 1 | $-13771.23 | -4.5% |
| **+10¢** | 36281 | 29023 | 7258 (99) | 1 | $-12625.23 | -5.5% |
| **+15¢** | 30391 | 22572 | 7819 (127) | 1 | $-11535.22 | -6.0% |
| **+20¢** | 27002 | 18809 | 8193 (166) | 1 | $-10185.71 | -6.0% |
| **+10¢ (15¢ stop)** | 59237 | 59144 | 93 (56) | 1 | $-21958.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 17:11 | +10 stop | BNB | DOWN | 0.55 | open |  |
| 11-05 17:10 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.13 |
| 11-05 17:09 | +10 stop | BNB | DOWN | 0.70 | 0.53 | -2.03 |
| 11-05 17:09 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-05 17:09 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:09 | +10 stop | BNB | DOWN | 0.48 | 0.61 | 0.95 |
| 11-05 17:09 | +10 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-05 17:09 | +5 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-05 17:06 | +5 | BNB | DOWN | 0.70 | 0.78 | 0.52 |
| 11-05 17:03 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 17:03 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 17:03 | +20 | XRP | DOWN | 0.64 | 0.86 | 1.94 |
| 11-05 17:03 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 11-05 17:03 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 17:03 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 17:02 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-05 17:01 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 17:01 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.90 |
| 11-05 17:01 | +15 | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 11-05 17:01 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 17:01 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 17:01 | +10 stop | BNB | DOWN | 0.71 | 0.51 | -2.33 |
| 11-05 17:01 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 17:01 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 11-05 17:01 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-05 17:01 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.89 |
| 11-05 17:01 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-05 17:01 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-05 17:01 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-05 17:01 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-05 17:01 | +20 | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 11-05 17:01 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-05 17:01 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-05 17:01 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 17:01 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 17:01 | +20 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-05 17:01 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-05 17:01 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
