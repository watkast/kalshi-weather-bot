# Range-Scalp Bot

*Updated Wed Nov 11 03:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55304 | 48230 | 7074 (94) | 2 | $-15115.34 | -4.3% |
| **+10¢** | 41312 | 33060 | 8252 (124) | 5 | $-14059.58 | -5.4% |
| **+15¢** | 34633 | 25739 | 8894 (158) | 7 | $-12804.45 | -5.9% |
| **+20¢** | 30837 | 21507 | 9330 (207) | 7 | $-11202.76 | -5.8% |
| **+10¢ (15¢ stop)** | 67355 | 67237 | 118 (73) | 0 | $-24836.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 03:04 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-11 03:04 | +10 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-11 03:04 | +5 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-11 03:03 | +10 stop | SOL | UP | 0.71 | 0.84 | 1.05 |
| 11-11 03:03 | +5 | SOL | UP | 0.71 | 0.84 | 1.05 |
| 11-11 03:03 | +10 stop | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 11-11 03:02 | +10 stop | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-11 03:02 | +10 stop | BTC | UP | 0.63 | 0.77 | 1.10 |
| 11-11 03:02 | +10 stop | NEAR | UP | 0.60 | 0.74 | 1.09 |
| 11-11 03:02 | +10 | NEAR | UP | 0.60 | 0.74 | 1.09 |
| 11-11 03:02 | +5 | NEAR | UP | 0.60 | 0.68 | 0.47 |
| 11-11 03:02 | +10 stop | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-11 03:02 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 11-11 03:02 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-11 03:02 | +20 | BNB | UP | 0.67 | 0.89 | 1.97 |
| 11-11 03:02 | +15 | BNB | UP | 0.67 | 0.82 | 1.23 |
| 11-11 03:02 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-11 03:02 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 11-11 03:02 | +5 | BTC | UP | 0.65 | 0.72 | 0.39 |
| 11-11 03:02 | +10 | SOL | DOWN | 0.50 | open |  |
| 11-11 03:02 | +5 | SOL | DOWN | 0.50 | 0.58 | 0.44 |
| 11-11 03:02 | +10 stop | XRP | DOWN | 0.41 | 0.54 | 0.95 |
| 11-11 03:02 | +20 | XRP | DOWN | 0.41 | open |  |
| 11-11 03:02 | +15 | XRP | DOWN | 0.41 | open |  |
| 11-11 03:02 | +10 | XRP | DOWN | 0.41 | 0.54 | 0.95 |
| 11-11 03:02 | +5 | XRP | DOWN | 0.41 | 0.54 | 0.95 |
| 11-11 03:01 | +10 stop | ETH | DOWN | 0.53 | 0.33 | -2.34 |
| 11-11 03:01 | +20 | ETH | DOWN | 0.53 | open |  |
| 11-11 03:01 | +15 | ETH | DOWN | 0.53 | open |  |
| 11-11 03:01 | +10 | ETH | DOWN | 0.53 | open |  |
| 11-11 03:01 | +5 | ETH | DOWN | 0.53 | 0.60 | 0.35 |
| 11-11 03:01 | +10 stop | ZEC | DOWN | 0.62 | 0.36 | -2.94 |
| 11-11 03:01 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-11 03:01 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-11 03:01 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-11 03:01 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-11 03:01 | +10 stop | BTC | DOWN | 0.51 | 0.34 | -2.04 |
| 11-11 03:01 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-11 03:01 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-11 03:01 | +10 | BTC | DOWN | 0.53 | open |  |
