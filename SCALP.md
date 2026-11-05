# Range-Scalp Bot

*Updated Thu Nov 05 02:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47939 | 41746 | 6193 (73) | 1 | $-13812.05 | -4.6% |
| **+10¢** | 35816 | 28627 | 7189 (99) | 2 | $-12640.83 | -5.6% |
| **+15¢** | 30009 | 22270 | 7739 (127) | 3 | $-11552.75 | -6.1% |
| **+20¢** | 26655 | 18551 | 8104 (166) | 6 | $-10197.67 | -6.1% |
| **+10¢ (15¢ stop)** | 58440 | 58347 | 93 (56) | 0 | $-21715.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 02:54 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 02:54 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 02:54 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-05 02:53 | +10 stop | DOGE | UP | 0.38 | 0.57 | 1.55 |
| 11-05 02:52 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 11-05 02:52 | +20 | SOL | DOWN | 0.69 | 0.92 | 2.10 |
| 11-05 02:52 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 11-05 02:52 | +10 | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 11-05 02:52 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-05 02:52 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-05 02:52 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-05 02:51 | +5 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-05 02:51 | +5 | BNB | DOWN | 0.70 | 0.83 | 1.00 |
| 11-05 02:50 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.22 |
| 11-05 02:50 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-05 02:50 | +10 stop | BTC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-05 02:50 | +10 stop | DOGE | DOWN | 0.69 | 0.43 | -2.93 |
| 11-05 02:50 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-05 02:50 | +10 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-05 02:50 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-05 02:50 | +5 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-05 02:50 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-05 02:50 | +15 | XRP | DOWN | 0.57 | 0.81 | 2.11 |
| 11-05 02:50 | +10 | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-05 02:50 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 11-05 02:49 | +10 stop | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-05 02:49 | +15 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-05 02:49 | +10 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
| 11-05 02:49 | +5 | ETH | DOWN | 0.58 | 0.66 | 0.46 |
| 11-05 02:49 | +10 stop | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-05 02:49 | +10 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-05 02:49 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-05 02:49 | +10 stop | BNB | DOWN | 0.64 | 0.83 | 1.68 |
| 11-05 02:49 | +10 | BNB | DOWN | 0.64 | 0.83 | 1.68 |
| 11-05 02:49 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.23 |
| 11-05 02:49 | +10 stop | NEAR | UP | 0.53 | 0.37 | -1.95 |
| 11-05 02:49 | +15 | NEAR | UP | 0.53 | open |  |
| 11-05 02:49 | +10 | NEAR | UP | 0.53 | open |  |
| 11-05 02:49 | +5 | NEAR | UP | 0.53 | 0.60 | 0.35 |
| 11-05 02:48 | +10 stop | BTC | UP | 0.63 | 0.47 | -1.95 |
