# Range-Scalp Bot

*Updated Mon Nov 02 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44176 | 38480 | 5696 (65) | 8 | $-12704.64 | -4.6% |
| **+10¢** | 32964 | 26378 | 6586 (86) | 9 | $-11483.56 | -5.5% |
| **+15¢** | 27591 | 20502 | 7089 (113) | 9 | $-10493.19 | -6.1% |
| **+20¢** | 24514 | 17092 | 7422 (147) | 9 | $-9227.25 | -6.0% |
| **+10¢ (15¢ stop)** | 53888 | 53802 | 86 (51) | 0 | $-20392.34 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 01:23 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-02 01:22 | +10 stop | BNB | DOWN | 0.53 | 0.30 | -2.63 |
| 11-02 01:22 | +10 | BNB | DOWN | 0.53 | open |  |
| 11-02 01:22 | +5 | BNB | DOWN | 0.53 | 0.61 | 0.45 |
| 11-02 01:22 | +10 stop | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 11-02 01:22 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-02 01:22 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 11-02 01:22 | +10 stop | XRP | UP | 0.69 | 0.82 | 1.04 |
| 11-02 01:21 | +10 stop | DOGE | DOWN | 0.61 | 0.39 | -2.54 |
| 11-02 01:20 | +10 stop | BTC | DOWN | 0.61 | 0.41 | -2.34 |
| 11-02 01:20 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-02 01:20 | +15 | BTC | DOWN | 0.61 | open |  |
| 11-02 01:20 | +10 | BTC | DOWN | 0.61 | open |  |
| 11-02 01:20 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-02 01:20 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 11-02 01:20 | +5 | SOL | DOWN | 0.71 | open |  |
| 11-02 01:20 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-02 01:20 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-02 01:20 | +10 stop | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
| 11-02 01:19 | +10 stop | NEAR | DOWN | 0.66 | 0.47 | -2.24 |
| 11-02 01:19 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-02 01:19 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-02 01:19 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-02 01:19 | +5 | NEAR | DOWN | 0.66 | open |  |
| 11-02 01:19 | +10 stop | ZEC | UP | 0.61 | 0.82 | 1.80 |
| 11-02 01:19 | +10 stop | ETH | DOWN | 0.61 | 0.43 | -2.15 |
| 11-02 01:19 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-02 01:19 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-02 01:19 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-02 01:18 | +5 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-02 01:18 | +10 stop | DOGE | UP | 0.67 | 0.46 | -2.44 |
| 11-02 01:18 | +10 stop | BTC | DOWN | 0.53 | 0.66 | 0.96 |
| 11-02 01:18 | +20 | BTC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-02 01:18 | +15 | BTC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-02 01:18 | +10 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-02 01:18 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-02 01:18 | +5 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-02 01:18 | +10 stop | ETH | DOWN | 0.52 | 0.62 | 0.65 |
| 11-02 01:18 | +20 | ETH | DOWN | 0.52 | open |  |
| 11-02 01:18 | +15 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
