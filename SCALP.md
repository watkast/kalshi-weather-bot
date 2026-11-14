# Range-Scalp Bot

*Updated Sat Nov 14 01:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58804 | 51308 | 7496 (106) | 2 | $-15877.91 | -4.3% |
| **+10¢** | 43932 | 35165 | 8767 (139) | 3 | $-14857.69 | -5.4% |
| **+15¢** | 36816 | 27371 | 9445 (174) | 3 | $-13446.64 | -5.8% |
| **+20¢** | 32797 | 22881 | 9916 (226) | 4 | $-11833.28 | -5.8% |
| **+10¢ (15¢ stop)** | 71591 | 71453 | 138 (82) | 2 | $-26354.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 01:06 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 11-14 01:06 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-14 01:06 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-14 01:06 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-14 01:06 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-14 01:06 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-14 01:06 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-14 01:06 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-14 01:06 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-14 01:06 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-14 01:06 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 11-14 01:05 | +10 stop | BNB | DOWN | 0.65 | 0.41 | -2.73 |
| 11-14 01:05 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-14 01:05 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-14 01:02 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 01:02 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-14 01:02 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-14 01:02 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.34 |
| 11-14 01:02 | +10 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-14 01:02 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 11-14 01:01 | +10 stop | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-14 01:01 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 01:01 | +15 | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 01:01 | +10 | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-14 01:01 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-14 01:01 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 01:01 | +20 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-14 01:01 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-14 01:01 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 01:01 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-14 01:01 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 01:01 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-14 01:01 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-14 01:01 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 01:01 | +5 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 00:58 | +5 | ETH | DOWN | 0.38 | 0.54 | 1.25 |
| 11-14 00:58 | +10 stop | ETH | DOWN | 0.40 | 0.54 | 1.05 |
| 11-14 00:56 | +10 stop | ETH | UP | 0.52 | 0.73 | 1.82 |
| 11-14 00:55 | +10 stop | BNB | DOWN | 0.60 | 0.35 | -2.83 |
| 11-14 00:55 | +10 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
