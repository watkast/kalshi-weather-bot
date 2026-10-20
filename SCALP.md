# Range-Scalp Bot

*Updated Tue Oct 20 18:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26038 | 22678 | 3360 (32) | 2 | $-7591.94 | -4.6% |
| **+10¢** | 19595 | 15710 | 3885 (47) | 4 | $-6730.64 | -5.5% |
| **+15¢** | 16403 | 12222 | 4181 (71) | 5 | $-6010.38 | -5.8% |
| **+20¢** | 14513 | 10131 | 4382 (90) | 7 | $-5394.52 | -5.9% |
| **+10¢ (15¢ stop)** | 31921 | 31868 | 53 (30) | 4 | $-11739.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 18:35 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 10-20 18:35 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-20 18:35 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-20 18:35 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-20 18:35 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-20 18:34 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 10-20 18:34 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-20 18:34 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-20 18:34 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-20 18:33 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-20 18:33 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 18:32 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-20 18:32 | +10 | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-20 18:32 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-20 18:32 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 18:31 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 18:31 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-20 18:31 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 18:31 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 18:31 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 18:31 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-20 18:31 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-20 18:31 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-20 18:31 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 18:31 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 10-20 18:31 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.92 |
| 10-20 18:31 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-20 18:31 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-20 18:31 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.92 |
| 10-20 18:31 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.61 |
| 10-20 18:31 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-20 18:31 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-20 18:31 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-20 18:31 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-20 18:31 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 18:31 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 0.98 |
| 10-20 18:31 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-20 18:31 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.40 |
| 10-20 18:31 | +10 | BNB | DOWN | 0.66 | 0.79 | 0.98 |
| 10-20 18:31 | +5 | BNB | DOWN | 0.66 | 0.79 | 0.98 |
