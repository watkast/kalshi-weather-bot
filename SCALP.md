# Range-Scalp Bot

*Updated Thu Nov 19 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64565 | 56323 | 8242 (124) | 1 | $-17549.40 | -4.3% |
| **+10¢** | 48231 | 38592 | 9639 (165) | 3 | $-16359.37 | -5.4% |
| **+15¢** | 40445 | 30054 | 10391 (210) | 5 | $-14775.83 | -5.8% |
| **+20¢** | 36017 | 25109 | 10908 (265) | 6 | $-13063.83 | -5.8% |
| **+10¢ (15¢ stop)** | 78569 | 78405 | 164 (98) | 1 | $-28895.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 01:56 | +5 | ZEC | UP | 0.67 | open |  |
| 11-19 01:56 | +15 | ZEC | UP | 0.71 | open |  |
| 11-19 01:56 | +10 | ZEC | UP | 0.71 | open |  |
| 11-19 01:56 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-19 01:56 | +10 stop | ZEC | DOWN | 0.45 | 0.63 | 1.46 |
| 11-19 01:56 | +20 | ZEC | DOWN | 0.45 | open |  |
| 11-19 01:56 | +15 | ZEC | DOWN | 0.45 | 0.63 | 1.46 |
| 11-19 01:56 | +10 | ZEC | DOWN | 0.45 | 0.63 | 1.46 |
| 11-19 01:56 | +5 | ZEC | DOWN | 0.45 | 0.63 | 1.46 |
| 11-19 01:56 | +10 stop | BTC | DOWN | 0.51 | 0.35 | -1.94 |
| 11-19 01:56 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-19 01:56 | +10 | BTC | DOWN | 0.51 | open |  |
| 11-19 01:56 | +5 | BTC | DOWN | 0.50 | 0.60 | 0.65 |
| 11-19 01:53 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-19 01:53 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 11-19 01:52 | +10 stop | XRP | DOWN | 0.54 | 0.74 | 1.68 |
| 11-19 01:51 | +5 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-19 01:51 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-19 01:51 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-19 01:50 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 11-19 01:50 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 01:49 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.50 |
| 11-19 01:48 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 11-19 01:48 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-19 01:48 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-19 01:48 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-19 01:48 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-19 01:48 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.04 |
| 11-19 01:48 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-19 01:48 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-19 01:48 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-19 01:48 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-19 01:48 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 11-19 01:48 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-19 01:46 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-19 01:46 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.81 |
| 11-19 01:46 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-19 01:46 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-19 01:46 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-19 01:46 | +10 stop | XRP | DOWN | 0.70 | 0.50 | -2.33 |
