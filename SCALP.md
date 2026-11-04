# Range-Scalp Bot

*Updated Wed Nov 04 20:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47523 | 41379 | 6144 (73) | 2 | $-13713.51 | -4.6% |
| **+10¢** | 35507 | 28379 | 7128 (98) | 2 | $-12542.89 | -5.6% |
| **+15¢** | 29740 | 22064 | 7676 (126) | 3 | $-11504.48 | -6.2% |
| **+20¢** | 26422 | 18382 | 8040 (166) | 5 | $-10172.88 | -6.1% |
| **+10¢ (15¢ stop)** | 57925 | 57832 | 93 (56) | 1 | $-21584.43 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 20:51 | +10 stop | NEAR | UP | 0.55 | open |  |
| 11-04 20:50 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 20:50 | +10 stop | NEAR | UP | 0.42 | 0.54 | 0.84 |
| 11-04 20:49 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.32 |
| 11-04 20:49 | +5 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 11-04 20:48 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 20:48 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-04 20:48 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-04 20:48 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-04 20:48 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-04 20:48 | +10 stop | ZEC | UP | 0.61 | 0.46 | -1.85 |
| 11-04 20:48 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 20:48 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-04 20:48 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-04 20:48 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 20:48 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 20:48 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 20:48 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-04 20:48 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 20:48 | +10 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-04 20:48 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-04 20:48 | +10 stop | BNB | DOWN | 0.56 | 0.75 | 1.58 |
| 11-04 20:48 | +20 | BNB | DOWN | 0.56 | 0.77 | 1.79 |
| 11-04 20:48 | +15 | BNB | DOWN | 0.56 | 0.75 | 1.58 |
| 11-04 20:48 | +10 | BNB | DOWN | 0.56 | 0.75 | 1.58 |
| 11-04 20:48 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 11-04 20:48 | +10 stop | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-04 20:48 | +20 | SOL | DOWN | 0.56 | 0.78 | 1.89 |
| 11-04 20:48 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-04 20:48 | +10 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-04 20:48 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 11-04 20:47 | +10 stop | NEAR | DOWN | 0.70 | 0.51 | -2.23 |
| 11-04 20:47 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-04 20:47 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-04 20:46 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 20:46 | +20 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-04 20:46 | +15 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-04 20:46 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 20:46 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-04 20:46 | +5 | NEAR | DOWN | 0.70 | open |  |
